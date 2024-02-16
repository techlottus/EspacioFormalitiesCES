# python modules
import requests

# services
from constants.identifiers_constants import SF_CORE
from services.logger_service import logger
# constants
from constants.services_urls import SF_CORE_URL
from constants.messages import sf_core_unavailable, unavailable_option
from services.set_responses_service import error_response


def get_sf_access_token(email: str, school: str):
    """
        Request to SF-Core an access token to access Salesforce's services
    """

    sf_core_with_school_url = SF_CORE_URL + '/' + school
    logger.debug(f"{email} - Requesting {SF_CORE} for access_token at: {sf_core_with_school_url}")
    try:
        sf_core_response = requests.get(sf_core_with_school_url)
        sf_core_response_json = sf_core_response.json()
        logger.debug(f"{email} - 'SF-Core' response: {sf_core_response_json},"
                     f" status-code: {sf_core_response.status_code}")
        access_token = sf_core_response_json['sfData']['accessToken']
        token_type = sf_core_response_json['sfData']['tokenType']
    except Exception as e:
        logger.error(f"{email} - An error occurred trying to communicate with 'SF-Core' service")
        logger.error(e)
        return error_response(
            503,
            sf_core_unavailable,
            unavailable_option
        ), 503
    else:
        logger.info(f"{email} - Sf-Core answered correctly with an access token")
        auth_header = token_type + ' ' + access_token
        return auth_header
