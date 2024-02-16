from pydantic import BaseModel, Field, validator
from constants.ssces_constants import SERVICE_ID, SERVICE_NAME, PAYLOAD_LIMIT_SIZE, MAX_LIMIT_SIZE
from constants.messages import unavailable_option, unavailable_service_info
from services.logger_service import logger
from services.set_responses_service import error_response


class Headers(BaseModel):
    service_id: str = Field(None)
    service_name: str = Field(None)


class BadRequest(BaseModel):
    error = {
        "id": 400,
        "name": "Bad Request",
        "message": "You have to provide a 'Service-Id, a 'Service-Name and an authorization access token."
    }


class Unauthorized(BaseModel):
    service = {
        "id": SERVICE_ID,
        "name": SERVICE_NAME
    }
    status = {}
    error = {
        "id": 401,
        "info": 'Invalid access token'
    }


class Forbidden(BaseModel):
    service = {
        "id": SERVICE_ID,
        "name": SERVICE_NAME
    }
    status = {}
    error = {
        "id": 403,
        "info": 'Expired access token'
    }


class NotFound(BaseModel):
    service = {
        "id": SERVICE_ID,
        "name": SERVICE_NAME
    }
    status = {
        "info": unavailable_option
    }
    error = {
        "id": 404,
        "info": "No se encontró la matrícula '12345' en salesforce"
    }


class UnavailableService(BaseModel):
    service = {
        "id": SERVICE_ID,
        "name": SERVICE_NAME
    }
    status = {
        "info": unavailable_service_info
    }
    error = {
        "id": 503,
        "info": "'Service-name' service unavailable"
    }
    data = {}


class Files(BaseModel):
    fileName: str = Field(...)
    fileBody: str = Field(...)
    fileType: str = Field(...)

    @validator('fileBody')
    def validate_size_of_file(cls, string_base_64, values, **kwargs):
        logger.debug(f"{cls.validate_size_of_file.__name__}() accessed")
        # get the approximate size in bytes of the original file that was encoded
        # https://en.wikipedia.org/wiki/Base64#Padding
        file_size = (len(string_base_64) - 814) / 1.37
        # validated 1MB max by file
        if file_size > int(PAYLOAD_LIMIT_SIZE):
            logger.error(f"The following file has exceeded the size: {values['fileName']}, with {file_size / 1048576:.2f} MB")
            return error_response(422, f'The file {values["fileName"]} '
                                       f'has exceded the maximum size with {file_size / 1048576:.2f} MB',
                                  f'The following file has exceeded the size: {values["fileName"]}'), 422

        return string_base_64


class CommonRequestBody(BaseModel):
    phoneNumber: str = Field(None)
    chargeAccepted: bool = Field(None)
    comments: str = Field(None)
    files: list[Files] = Field(None)

    @validator('files')
    def validate_total_files_size(cls, list_files_base64: list[Files], values, **kwargs):
        logger.debug(f"{cls.validate_total_files_size.__name__}() accessed")
        max_limit = int(MAX_LIMIT_SIZE)
        total_files_size = 0

        for file in list_files_base64:
            file_size = (len(file.fileBody) - 814) / 1.37
            total_files_size = total_files_size + file_size

        logger.info(f'The set of files size is: {total_files_size / 1048576:.2f} MB')
        # validated 5MB max by total files
        if total_files_size > max_limit:
            logger.error(f"The set of files exceeded the maximum total allowed 5MB with {total_files_size / 1048576:.2f} MB")
            return error_response(422, f'The set of files exceeded the maximum total allowed 5MB with {total_files_size / 1048576:.2f} MB')
