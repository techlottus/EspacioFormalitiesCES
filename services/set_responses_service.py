# python modules
import copy
import json
from flask import Response
from werkzeug.exceptions import abort
# constants
from constants.identifiers_constants import status_key, data_key, info_key, transactionNumber_key, id_key, error_key
from constants.ssces_constants import sscesResponse
# services
from services.logger_service import logger


def error_response_auth(status_code: int, error_info: str, status_info: str = None):
    """
    Sets Error Response
    """
    error_response_obj = copy.deepcopy(sscesResponse)
    if status_info is not None:
        error_response_obj[status_key] = {
            info_key: status_info
        }
    error_response_obj[error_key] = {
        id_key: status_code,
        info_key: error_info
    }
    return error_response_obj


def error_response(status_code: int, error_info: str, status_info: str = None):
    """
    Sets Error Response
    """
    error_response_obj = copy.deepcopy(sscesResponse)
    if status_info is not None:
        error_response_obj[status_key] = {
            info_key: status_info
        }
    error_response_obj[error_key] = {
        id_key: status_code,
        info_key: error_info
    }
    return abort(Response(json.dumps(error_response_obj), mimetype='application/json', status=status_code)), status_code


def successful_response_get_method(data, status_info):
    ok_response = copy.deepcopy(sscesResponse)
    ok_response[data_key] = data
    ok_response[status_key] = {
        id_key: 200,
        info_key: status_info
    }
    return ok_response, 200


def successful_response_post_method(
        email: str,
        ticket_number: str,
        transaction_number: str,
        procedure: str
):
    """
    Sets Successful Response
    """
    logger.debug(f"{email} - Salesforce response was successful")
    status_info = f"'{procedure}' was successfully requested to Salesforce service"
    logger.info(f"{email} - SSCES answered correctly with a ticket number and a transaction number")
    ok_response = copy.deepcopy(sscesResponse)
    ok_response[data_key] = {
        "ticketNumber": ticket_number,
        transactionNumber_key: transaction_number
    }
    ok_response[status_key] = {
        id_key: 201,
        info_key: status_info
    }
    return ok_response, 201
