import requests
# interfaces
from interfaces.interfaces import StudentData
# services
from services.logger_service import logger
from services.set_responses_service import error_response
from services.sf_core_service import get_sf_access_token
# constants
from constants.messages import unavailable_option, sf_servicios_escolares_unavailable, unavailable_service_info
from constants.identifiers_constants import UTC, ULA, SF_SERVICIOS_ESCOLARES, Authorization, tickets_key, message_key, \
    error_key, ticket_key, SF_PICKLIST, picklist_key
from constants.services_urls import SF_SERVICIOS_ESCOLARES_URL_UTC, SF_SERVICIOS_ESCOLARES_URL_ULA, SF_PICKLIST_URL_ULA


def fetch_picklist(
        email: str,
        pick_list_name: str,
        record_type_name: str,
        sf_auth_header: str,
):
    logger.debug(f"{email} - {fetch_picklist.__name__}() accessed")
    # response sales force
    full_picklist_url = SF_PICKLIST_URL_ULA + '?namePickList=' + pick_list_name
    headers = {Authorization: sf_auth_header}
    try:
        logger.debug(
            f"{email} - Trying to fetch '{pick_list_name}' picklist for '{record_type_name}'"
            f"record type at {full_picklist_url}"
        )
        sf_response = requests.get(full_picklist_url, headers=headers)
        status_code = sf_response.status_code
        sf_response_json = sf_response.json()

        logger.debug(f"{email} - {SF_PICKLIST} response: {sf_response_json}; statusCode: {status_code}")
        # pick_list_array = sf_response_json["picklist"]
        # return pick_list_array

    except Exception as e:
        error_message = f"Something wrong happened fetching ${pick_list_name} picklist for '{record_type_name}' " \
                        f"record type: ${e} "
        logger.error(f"{email} - {error_message}")
        exception_string = str(type(e)) + ': ' + str(e)
        logger.error(f"{email} - {exception_string}")
        return error_response(
            503,
            exception_string,
            error_message
        )
    else:
        sf_response_keys = [picklist_key, message_key, error_key]
        if sf_errors_handler(email, sf_response_json, status_code, sf_response_keys) is False:
            logger.info(f"{email} - {pick_list_name} picklist for '${record_type_name}' record type fetched.")
            return sf_response_json[picklist_key]


def request_procedure_to_salesforce(
        student_data: StudentData,
        procedure: str,
        sf_request_body: dict
):
    """
    Request a procedure to Salesforce "ServiciosEscolares" service
    """

    email = student_data.email
    logger.debug(f"{email} - {request_procedure_to_salesforce.__name__} accessed")

    # REQUEST SF-CORE FOR SF_ACCESS_TOKEN
    school = student_data.school
    authorization_header = get_sf_access_token(email, school)
    sf_headers = {Authorization: authorization_header}

    if school == UTC:
        sf_school_services = SF_SERVICIOS_ESCOLARES_URL_UTC
    elif school == ULA:
        sf_school_services = SF_SERVICIOS_ESCOLARES_URL_ULA
    else:
        return error_response(404, f"School '{school}' is not handled by this API", unavailable_option)

    logger.debug(f"{email} - Requesting '{procedure}' to Salesforce at: {sf_school_services}")
    req_body_without_files = {key: val for key, val in sf_request_body.items() if key != "files"}
    logger.debug(f"{email} - Request body without files key: {req_body_without_files}")

    try:
        sf_response = requests.post(
            sf_school_services,
            headers=sf_headers,
            json=sf_request_body
        )
        status_code = sf_response.status_code
        sf_response_json = sf_response.json()
        logger.info(f"{email} - {SF_SERVICIOS_ESCOLARES} response: {sf_response_json}; statusCode: {status_code}")

    except Exception as e:
        error_message = f"An error occurred attempting to communicate with {SF_SERVICIOS_ESCOLARES} service"
        logger.error(f"{email} - {error_message}")
        exception_string = str(type(e)) + ': ' + str(e)
        logger.error(f"{email} - {exception_string}")
        return error_response(
            503,
            exception_string,
            error_message
        )
    else:
        sf_response_keys = [ticket_key, message_key, error_key]
        if sf_errors_handler(email, sf_response_json, status_code, sf_response_keys) is False:
            return sf_response_json[ticket_key]


def request_all_tickets_to_salesforce(
        email: str,
        school: str,
        sf_tickets_url: str,
):
    logger.debug(f"{email} - {request_all_tickets_to_salesforce.__name__} accessed")
    auth_header = get_sf_access_token(email, school)
    sf_authorization_header = {Authorization: auth_header}
    try:
        logger.debug(f"{email} - Requesting salesforce for student's tickets data at: {sf_tickets_url}")
        sf_tickets_response = requests.get(sf_tickets_url, headers=sf_authorization_header)
        status_code = sf_tickets_response.status_code
        logger.info(f"{email} - 'Request to {SF_SERVICIOS_ESCOLARES} statusCode: {status_code}")
        tickets_response_json = sf_tickets_response.json()
        logger.info(f"{email} - {SF_SERVICIOS_ESCOLARES} response body: {tickets_response_json}")
    except Exception as e:
        logger.error(f"{email} - An error occurred attempting to communicate with {SF_SERVICIOS_ESCOLARES} service")
        logger.error(f"{email} - {e}")
        return error_response(
            503,
            sf_servicios_escolares_unavailable,
            unavailable_option
        )
    else:
        sf_response_keys = [tickets_key, message_key, error_key]
        if sf_errors_handler(email, tickets_response_json, status_code, sf_response_keys) is False:
            return tickets_response_json[tickets_key]


def sf_errors_handler(email, sf_response, status_code, sf_response_keys):
    """
    Salesforce's response error handler
    """
    logger.debug(f"{email} - {sf_errors_handler.__name__}() accessed")
    # check if sf response is a list (unexpected)
    if type(sf_response) == list:
        error_message = "Salesforce's response is a list not a dictionary"
        logger.fatal(f"{email} - {error_message}")
        sf_response = sf_response[0]
        if type(sf_response) is dict:
            error_code = 'errorCode'
            if message_key in sf_response.keys() and error_code in sf_response.keys():
                error_message = f"Salesforce error message: {sf_response[error_code]}: {sf_response[message_key]}"
                logger.error(f"{email} - {error_message}")
        return error_response(
            503,
            error_message,
            unavailable_option
        )
    if type(sf_response) is not dict:
        error_message = "Salesforce's response is not a dictionary"
        logger.fatal(f"{email} - {error_message}")
        info_message = unavailable_option
        return error_response(
            503,
            error_message,
            info_message
        )
    # check if some key is not in sf response
    for key in sf_response_keys:
        if key not in sf_response.keys():
            error_message = f"Unexpected salesforce's response, '{key}' key does not exist"
            logger.error(f"{email} - {error_message}")
            return error_response(
                503,
                error_message,
                unavailable_option
            )
    # check error key is equal to true
    if sf_response[error_key]:
        error_message = 'Salesforce error message: ' + sf_response[message_key]
        logger.error(f"{email} - {error_message}")
        return error_response(
            status_code,
            error_message,
            unavailable_option
        )
    # this is reached if no error was found
    else:
        return False
