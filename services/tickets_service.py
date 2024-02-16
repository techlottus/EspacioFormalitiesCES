# python modules
import json

import requests
import datetime as dt
# constants
from constants.identifiers_constants import PAYMENT_SERVICE_ID, PAYMENT_SERVICE_NAME, numticket_key, Authorization, \
    Service_Id, transactionNumber_key, data_key, ticket_key, id_key, tickets_key
from constants.messages import unavailable_service_info, unavailable_option, payments_unavailable
from constants.services_urls import SF_REQUEST_TICKETS_URL_UTC, SF_REQUEST_TICKETS_URL_ULA, PAYMENTS_GET_TRANSACTION_URL
from constants.identifiers_constants import UTC, ULA
# services
from services.logger_service import logger
from services.set_responses_service import error_response
# repositories
from repositories.keys_repository import keys_repository
from repositories.ADS_Scores_Medallia_repository import scores_repository


def get_sf_tickets_url(school: str):
    """
    SET TICKETS URL BASED ON SCHOOL
    """
    if school == UTC:
        return SF_REQUEST_TICKETS_URL_UTC
    elif school == ULA:
        return SF_REQUEST_TICKETS_URL_ULA
    else:
        return error_response(404, f"School '{school}' is not handled by this API", unavailable_option)


def get_sf_tickets_url_with_record_types(
        email: str,
        school: str,
        enrollment_number: str
):
    """
    SETS FULL TICKETS URL WITH RECORD TYPES
    """
    logger.debug(f"{email} - {get_sf_tickets_url_with_record_types.__name__}() accessed")
    sf_url = get_sf_tickets_url(school)
    # RECORDS OF KEYS REPOSITORY
    query, query_filter = {"school": school, "recordTypeId": True}, {'key': 1, 'description': 1, '_id': 0}
    record_type_object_array = keys_repository().find(query, query_filter)
    record_type_list = list(record_type_object_array)
    logger.debug(f'{email} - {len(record_type_list)} Record types found: {record_type_list}')

    records = ''
    for record_object in record_type_list:
        records += record_object['key'] + ","

    # REQUEST SALESFORCE FOR TICKETS ARRAY
    sf_tickets_url = str(sf_url) + enrollment_number + "&records=" + records
    logger.info(f"{email} - sf_tickets_url set")
    return sf_tickets_url


def set_tickets_list_with_medallia_flags(
        email: str,
        sf_tickets_list
):
    """
    - filter tickets with null ticket number
    - set medallia flags
    """
    logger.debug(f"{email} - Total tickets retrieved: {len(sf_tickets_list)}")
    # GET LIST OF EVALUATED TICKETS IN MEDALLIA
    records_scores = list(scores_repository().find({"email": email, "microServices": "ProceduresServices"}))
    valid_tickets = []
    for ticket in sf_tickets_list:
        if ticket[numticket_key] is None:
            logger.warning(f"{email} - ticket with data: {ticket} doesn't have a ticket number")
            continue
        # set medallia flags
        ticket["microServices"] = "ProceduresServices"
        ticket_evaluated = next(
            (True for obj in records_scores if obj.get(numticket_key) == ticket[numticket_key]),
            False
        )
        ticket["evaluationFlag"] = True if ticket_evaluated else False
        valid_tickets.append(ticket)
    total_tickets_with_flags = len(valid_tickets)
    logger.debug(f"{email} - Total tickets with medallia flags: {total_tickets_with_flags}")
    return valid_tickets, total_tickets_with_flags


def set_payments_request_body(
        email: str,
        valid_tickets,
):
    """
    Sets request body to send to payments service
    """
    logger.debug(f"{email} - {set_payments_request_body.__name__} accessed")

    ticket_numbers_list = []
    for ticket in valid_tickets:
        ticket_numbers_list.append(ticket[numticket_key])

    request_body = {
        "service": {
            id_key: PAYMENT_SERVICE_ID,
            "name": PAYMENT_SERVICE_NAME
        },
        data_key: {
            tickets_key: ticket_numbers_list
        }
    }
    return request_body


def fetch_tickets_transaction_numbers(
        email: str,
        auth_header: str,
        request_body: dict
):
    """
    Consumes payments service to retrieve all transaction numbers from the tickets
    """
    # SEND TICKETS ARRAY TO 'PAYMENTS' SERVICE TO RETRIEVE TRANSACTION NUMBER
    headers = {
        Service_Id: PAYMENT_SERVICE_ID,
        Authorization: auth_header
    }
    try:
        logger.debug(
            f"{email} - Requesting 'transactionNumbers' to 'payments' service at {PAYMENTS_GET_TRANSACTION_URL}"
        )
        logger.debug(f"{email} - Request body sent: {request_body}")
        payments_response = requests.post(PAYMENTS_GET_TRANSACTION_URL,
                                          headers=headers,
                                          json=request_body
                                          )
        payments_response_json = payments_response.json()
        status_code = payments_response.status_code
        logger.debug(f"{email} - payments response: {payments_response_json}; statusCode: {status_code}")
    except Exception as e:
        logger.error(f"{email} - {payments_unavailable}")
        logger.error(f"{email} - {str(e)}")
        return error_response(503, payments_unavailable, unavailable_service_info)
    else:
        if status_code == 403:
            error_message = 'Payments service answer: Access token has expired'
            logger.error(f"{email} - {error_message}")
            return error_response(403, error_message)
        elif status_code >= 400:
            error_message = "'Payments' service rejected the request for transactionNumbers"
            logger.error(error_message)
            return error_response(400, error_message)
        elif data_key not in payments_response_json.keys():
            error_message = "Payments response format is unexpected"
            logger.error(error_message)
            return error_response(500, error_message)
        else:
            payments_data = payments_response_json[data_key]
            payments_response_length = len(payments_data)
            logger.info(f"{email} - 'Payments' service answered correctly with array of "
                        f"{payments_response_length} tickets")
            return payments_data, payments_response_length


def set_trans_nums_to_tickets_list(
        email,
        tickets_list,
        trans_numbers_dict_list
):
    """
    SETS TRANSACTION NUMBERS TO VALID TICKETS LIST
    """
    for ticket in tickets_list:
        ticket_number = ticket[numticket_key]
        payments_obj = next((obj for obj in trans_numbers_dict_list if obj[ticket_key] == ticket_number), None)
        if payments_obj is None:
            error_message = f"There is no ticket with ticket number {ticket_number} in payments response list"
            logger.error(error_message)
            return error_response(500, error_message, "Service unable to set transaction number to tickets list")
        if payments_obj[transactionNumber_key] == -1:
            logger.warn(f"{email} - ticket with ticket number '{ticket_number}' has no transaction number")
            ticket[transactionNumber_key] = None
        else:
            ticket[transactionNumber_key] = payments_obj[transactionNumber_key]
    logger.debug(f"{email} - tickets array with transaction number: {tickets_list}")
    return tickets_list
