# python modules
from flask_openapi3 import APIBlueprint, Tag
from flask import request as req
# OpenAPI
from OpenAPI.commons import BadRequest, Unauthorized, Forbidden, NotFound, UnavailableService, Headers, \
    CommonRequestBody
from OpenAPI.equivalence_studies_openapi import EquivalenceStudiesResponse
# constants
from constants.routes import EQUIVALENCE_ROUTE
from constants.identifiers_constants import equivalence_of_study, Authorization
# services
from services.logger_service import logger
from services.set_servicio_fields import set_servicio_properties
from services.set_responses_service import successful_response_post_method
from services.salesforce_requests_service import request_procedure_to_salesforce
from services.transaction_number_service import get_transaction_number
from services.fetch_keys_service import fetch_record_type, fetch_detail_code
# utilities
from utils.decoder import get_student_data

equivalence_of_studies = APIBlueprint(
    'equivalence_of_studies',
    __name__,
    url_prefix=EQUIVALENCE_ROUTE,
    abp_tags=[Tag(name="Equivalence of Studies",
                  description="'Equivalencia de estudios' procedure")],
    abp_responses={
        "400": BadRequest,
        "401": Unauthorized,
        "403": Forbidden,
        "404": NotFound,
        "503": UnavailableService
    }
)


@equivalence_of_studies.post('', responses={"200": EquivalenceStudiesResponse},
                             security=[{"jwt": []}])
def equivalence_of_studies_controller(header: Headers, body: CommonRequestBody):
    """
    Endpoint to request "Equivalencia de Estudios" to salesforce
    """
    auth_header = req.headers[Authorization]
    student_data = get_student_data(auth_header)
    email = student_data.email
    logger.debug(f"{email} - Controller accessed.")

    # SET "SERVICIO" PROPERTIES
    servicio_object = set_servicio_properties(student_data, body, equivalence_of_studies.name)

    # fetch record type
    record_type = fetch_record_type(student_data, equivalence_of_study)

    # SET SALESFORCE REQUEST BODY
    sf_request_body = {
        "servicio": [servicio_object.__dict__],
        "files": req.json['files'],  # json.dumps(body.files, default=pydantic_encoder))
        "matricula": servicio_object.Matricula__c,
        "recordtype": record_type
    }

    # SEND REQUEST TO SALESFORCE
    procedure = 'Equivalencia de Estudios'
    ticket_number = request_procedure_to_salesforce(
        student_data,
        procedure,
        sf_request_body,
    )

    # REQUEST TRANSACTION NUMBER TO "PAYMENTS" SERVICE
    detail_code = fetch_detail_code(student_data, equivalence_of_study)
    transaction_number = get_transaction_number(
        student_data,
        auth_header,
        ticket_number,
        detail_code
    )

    return successful_response_post_method(email, ticket_number, transaction_number, procedure)
