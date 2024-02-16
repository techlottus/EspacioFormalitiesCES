import requests
# constants
from constants.identifiers_constants import PAYMENT_SERVICE_ID, PAYMENT_SERVICE_NAME, Authorization, Service_Id
from constants.services_urls import COSTS_SERVICE_URL

# services
from services.logger_service import logger
from services.set_responses_service import error_response


def get_costs_of_detail_ids(email: str, auth_header: str, detail_id_array):
    logger.debug(f"{email} - {get_costs_of_detail_ids.__name__}() accessed")
    # request body cost
    costs_body = {
        "service": {
            "id": PAYMENT_SERVICE_ID,
            "name": PAYMENT_SERVICE_NAME
        },
        "data": {
            "detailCodes": detail_id_array
        }
    }
    headers = {
        Authorization: auth_header,
        Service_Id: PAYMENT_SERVICE_ID
    }
    logger.debug(f"{email} - costsBody: {costs_body}")
    costs_array: []
    try:
        logger.info(f"{email} - Trying to get procedures costs from 'paymentb9 service' at {COSTS_SERVICE_URL}")
        costs_response = requests.post(COSTS_SERVICE_URL, headers=headers, json=costs_body)
        costs_response_json = costs_response.json()
        status_code = costs_response.status_code
        costs_array = costs_response_json["data"]
        if costs_array:
            logger.info(f"{email} - Costs service answered correctly with costs array: {costs_array} with statusCode: "
                        f"{status_code}")
        else:
            logger.error(f"{email} - Costs array couldn't be retrieved from 'paymentsb9' service.")
            return error_response(503, "'paymentb9' service is not available")
    except Exception as e:
        error_message = "'paymentb9' service is not available"
        logger.error(f"{email} - {error_message}")
        return error_response(503, error_message), 503
    else:
        return costs_array


