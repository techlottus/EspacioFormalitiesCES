# python modules
import requests
# constants
from constants.messages import payments_unavailable, payments_unavailable_info
from constants.identifiers_constants import PAYMENT_SERVICE_ID, PAYMENT_SERVICE_NAME
# services
from constants.services_urls import PAYMENTS_ADD_TRANSACTION_URL
from interfaces.interfaces import StudentData
from services.logger_service import logger
from services.set_responses_service import error_response


def get_transaction_number(
        student_data: StudentData,
        auth_header,
        ticket_number,
        code_detail_id
    ):
    """
    retrieves transactionNumber for procedures.
    """
    email = student_data.email

    # consume "payments service" for transactionNumber
    request_body = {
        "service": {
            "id": PAYMENT_SERVICE_ID,
            "name": PAYMENT_SERVICE_NAME
        },
        "data": {
            "userId": student_data.studentId,
            "ticket": ticket_number,
            "detailId": code_detail_id,
            "periodCode": student_data.periodCode
        }
    }

    payments_headers = {
        "Authorization": auth_header,
        "Service-Id": PAYMENT_SERVICE_ID
    }
    logger.debug(f"{email} - Trying to communicate with 'payments' service to register procedure at:"
                 f"{PAYMENTS_ADD_TRANSACTION_URL}")
    logger.debug(f"{email} - Request body sent: {request_body}")
    try:
        payments_response = requests.post(PAYMENTS_ADD_TRANSACTION_URL, headers=payments_headers, json=request_body)
        payments_response_json = payments_response.json()
        logger.debug(f"{email} - payments response: {payments_response_json}, status_code: {payments_response.status_code}")
        transaction_number = payments_response_json['data']['transactionNumber']
    except Exception as e:
        logger.error(f"{email} - An error occurred attempting to communicate with payments service")
        logger.error(e)
        return error_response(404, payments_unavailable, payments_unavailable_info), 404
    else:
        logger.info(f'{email} - Payments service answered correctly with transaction number: {transaction_number}')
        return transaction_number
