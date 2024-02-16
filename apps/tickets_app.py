# python modules
from flask_openapi3 import APIBlueprint, Tag
from flask import request as req
# OpenAPI
from OpenAPI.commons import BadRequest, Unauthorized, Forbidden, NotFound, UnavailableService, Headers
from OpenAPI.tickets_openapi import TicketsResponse
# constants
from constants.identifiers_constants import Authorization
from constants.routes import TICKETS_ROUTE
# services
from services.logger_service import logger
from services.salesforce_requests_service import request_all_tickets_to_salesforce
from services.set_responses_service import successful_response_get_method
from services.tickets_service import get_sf_tickets_url_with_record_types, set_payments_request_body, \
    set_tickets_list_with_medallia_flags, fetch_tickets_transaction_numbers, set_trans_nums_to_tickets_list
# utils
from utils.decoder import get_student_data

# define API blueprint
tickets_api = APIBlueprint(
    'tickets_api',
    __name__,
    url_prefix=TICKETS_ROUTE,
    abp_tags=[Tag(name="Request all Tickets", description="Request all tickets to SF service and show them all to user")],
    abp_responses={
        "400": BadRequest,
        "401": Unauthorized,
        "403": Forbidden,
        "404": NotFound,
        "503": UnavailableService
    }
)


@tickets_api.get('', responses={"200": TicketsResponse}, security=[{"jwt": []}])
def tickets_controller(header: Headers):
    """
    Endpoint that returns array of all student's tickets data
    """
    auth_header = req.headers[Authorization]
    student_data = get_student_data(auth_header)
    email = student_data.email
    school = student_data.school

    logger.debug(f"{email} - {tickets_controller.__name__} accessed")
    enrollment_number = student_data.enrollmentNumber

    sf_tickets_url = get_sf_tickets_url_with_record_types(
        email,
        school,
        enrollment_number
    )

    sf_tickets_array = request_all_tickets_to_salesforce(email, school, sf_tickets_url)

    valid_tickets, total_valid_tickets = set_tickets_list_with_medallia_flags(email, sf_tickets_array)
    if total_valid_tickets == 0:
        info_message = "This user doesn't have any tickets yet, empty array sent"
        logger.info(f"{email} - {info_message}")
        return successful_response_get_method(valid_tickets, info_message)
    request_body = set_payments_request_body(email, valid_tickets)

    trans_numbers_dict_list, payments_response_length = fetch_tickets_transaction_numbers(
        email,
        auth_header,
        request_body
    )
    if total_valid_tickets != payments_response_length:
        logger.warning(f"{email} - salesforce tickets array is not equal to payments tickets array")
    
    # set transactionNumber to tickets array
    tickets_with_trans_nums_list = set_trans_nums_to_tickets_list(
        email,
        valid_tickets,
        trans_numbers_dict_list
    )

    # SEND RESPONSE
    info_message = f"List of {total_valid_tickets} tickets with transaction number sent"
    logger.info(f"{email} - {info_message}")
    return successful_response_get_method(tickets_with_trans_nums_list, info_message)
