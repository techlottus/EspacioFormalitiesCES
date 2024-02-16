from constants.identifiers_constants import ULA, EJECUTIVA, DISTANCIA, school_key, procedure_key
from constants.collections_constants import KEYS_COLLECTION_NAME, DETAIL_CODES_COLLECTION_NAME
from interfaces.interfaces import StudentData
from repositories.keys_repository import keys_repository
from repositories.detail_codes_repository import detail_codes_repository
from services.logger_service import logger
from services.set_responses_service import error_response


def fetch_record_type(student_data: StudentData, identifier: str):
    """
    Fetches procedure record type
    """
    email = student_data.email
    school = student_data.school
    filter_params = {
        school_key: school,
        "identifier": identifier
    }
    if school == ULA:
        modality = student_data.modality
        if modality == EJECUTIVA:
            modality = DISTANCIA
        filter_params['modality'] = modality
    logger.debug(f"{email} - Fetching record type at '{KEYS_COLLECTION_NAME}' collection with {filter_params}")
    key_document = keys_repository().find_one(filter_params)
    if not key_document:
        error_message = f'No record type id found with this params: {filter_params}'
        logger.debug(f"{email} - {error_message}")
        return error_response(404, error_message, error_message), 404

    record_type = key_document['key']
    logger.debug(f"{email} - Record type id fetched: {record_type}")
    return record_type


def fetch_detail_code(student_data: StudentData, procedure: str):
    email = student_data.email
    school = student_data.school
    filter_params = {
        school_key: school,
        procedure_key: procedure
    }
    if school == ULA:
        modality = student_data.modality
        if modality == EJECUTIVA:
            modality = DISTANCIA
        filter_params['modality'] = modality
    logger.debug(f"{email} - Fetching detail code at '{DETAIL_CODES_COLLECTION_NAME}' collection with {filter_params}")
    detail_code_document = detail_codes_repository().find_one(filter_params)
    if not detail_code_document:
        error_message = f"No detail code document found at '{DETAIL_CODES_COLLECTION_NAME}' collection for "\
                        f"'{filter_params}'"
        logger.debug(f"{email} - {error_message}")
        return error_response(
            404,
            error_message,
            "Service was unable to request transaction number because detail code couldn't be fetched"
        )

    detail_code = detail_code_document['detailCode']
    logger.debug(f"{email} - Detail code fetched: {detail_code}")
    return detail_code
