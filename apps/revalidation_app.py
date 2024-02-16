# python modules
from flask_openapi3 import APIBlueprint, Tag
from flask import request as req
# OpenAPI
from OpenAPI.commons import BadRequest, Unauthorized, Forbidden, NotFound, UnavailableService, Headers
from OpenAPI.revalidation_openapi import RevalidationResponse, RevalidationRequestBody
# CONSTANTS
from constants.routes import REVALIDATION_ROUTE
from constants.identifiers_constants import revalidation_id, ULA
# services
from services.fetch_keys_service import fetch_record_type, fetch_detail_code
from services.logger_service import logger
from services.set_servicio_fields import set_servicio_properties
from services.set_responses_service import successful_response_post_method
from services.salesforce_requests_service import request_procedure_to_salesforce
from services.transaction_number_service import get_transaction_number
from utils.decoder import get_student_data

revalidation = APIBlueprint(
    'Revalidation',
    __name__,
    url_prefix=REVALIDATION_ROUTE,
    abp_tags=[Tag(name="Revalidation", description="'Revalidation' procedure")],
    abp_responses={
        "400": BadRequest,
        "401": Unauthorized,
        "403": Forbidden,
        "404": NotFound,
        "503": UnavailableService
    }
)


@revalidation.post('', responses={"201": RevalidationResponse},
                    security=[{"jwt": []}])
def revalidation_controller(header: Headers, body: RevalidationRequestBody):
    """
    Endpoint to request "Revalidación de Estudios" procedure to salesforce
    """

    auth_header = req.headers['Authorization']
    student_data = get_student_data(auth_header)
    email = student_data.email
    logger.debug(f"{email} -  Controller accessed")

    # SET "SERVICIO" PROPERTIES
    servicio_response = set_servicio_properties(student_data, body, revalidation.name)
    # fetch record type
    record_type = fetch_record_type(student_data, revalidation_id)

    print()
    # SET SALESFORCE REQUEST BODY
    sf_request_body = {
        "servicio": [servicio_response.__dict__],
        "files": req.json['files'],
        "matricula": servicio_response.Matricula__c,
        "recordtype": record_type
    }

    # SEND REQUEST TO SALESFORCE
    procedure = 'Revalidación'
    ticket_number = request_procedure_to_salesforce(
        student_data,
        procedure,
        sf_request_body,
    )

    # SEND RESPONSE
    if student_data.school == ULA:
        # REQUEST TRANSACTION NUMBER TO "PAYMENTS" SERVICE
        detail_code = fetch_detail_code(student_data, revalidation_id)

        transaction_number = get_transaction_number(
            student_data,
            auth_header,
            ticket_number,
            detail_code
        )
        logger.debug(f"{email} - transaction_number: {transaction_number}")
        return successful_response_post_method(email, ticket_number, transaction_number, procedure)
    return successful_response_post_method(email, ticket_number, None, procedure)
