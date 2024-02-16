# python modules
from jwt import decode
# services
from interfaces.interfaces import StudentData
# interfaces
from services.logger_service import logger
from services.set_responses_service import error_response


def token_decoder(authorization_header):
    """
    Decodes Access Token from 'Authorization' header
    """
    logger.debug("Decoding access token.")
    try:
        access_token = authorization_header.replace("Bearer ", "")
        decoded = decode(access_token, options={"verify_signature": False})
    except Exception as e:
        logger.error("Something went wrong decoding access token")
        logger.error(f" Exception type: {type(e)}")
        logger.error(e)
        return error_response(403, "Something went wrong decoding access token")
    else:
        logger.debug(f"Token decoded successfully")
        return decoded


def get_student_data(auth_header):
    decoded_token = token_decoder(auth_header)

    try:
        student_data = StudentData()
        student_data.enrollmentNumber = decoded_token["studentEnrollmentNumber"]
        student_data.name = decoded_token["name"]
        student_data.email = decoded_token["email"]
        student_data.phoneNumber = decoded_token["phoneNumber"]
        student_data.campus = decoded_token["campus"]
        student_data.program = decoded_token["program"]
        student_data.level = decoded_token["academicLevel"]
        student_data.levelCode = decoded_token["academicLevelCode"]
        student_data.modality = decoded_token["modality"]
        student_data.studentId = decoded_token["studentId"]
        student_data.periodCode = decoded_token["periodCode"]
        student_data.school = decoded_token["webApp"]["school"]
        student_data.cuatrimestre = decoded_token["cuatrimestre"]
    except Exception as e:
        logger.fatal(f"Error: {e}")
        return error_response(400, f"Some properties couldn't be fetched from accessToken: {e}",
                              f"Some properties couldn't be fetched from accessToken: {e}")
    else:
        logger.debug(f"{student_data.email} - StudentData: {student_data.__dict__}")
        return student_data
