# python modules
from flask_openapi3 import APIBlueprint, Tag
from flask import request as req
# OpenAPI
from OpenAPI.commons import BadRequest, Unauthorized, Forbidden, NotFound, UnavailableService, Headers
from OpenAPI.degree_openapi import DegreResponseGet, DegreResponsePost, RequestBodyDegree
# constants
from constants.routes import DEGREE_ROUTE
from constants.degree_constants import degreeType
from constants.identifiers_constants import DISTANCIA, ESCOLARIZADA, Authorization
# services
from services.logger_service import logger
from services.programs_service import get_programs_detail, format_programs
from services.set_servicio_fields import set_servicio_properties
from services.update_collections_service import check_if_update_needed_in_degree_procedure_records
from services.degree_service import fetch_degree_record_detail_code, get_list_detail_codes, generate_record_types, \
    get_all_detail_codes
from services.salesforce_requests_service import request_procedure_to_salesforce
from services.set_responses_service import successful_response_post_method, successful_response_get_method, \
    error_response
from services.transaction_number_service import get_transaction_number
from services.costs_service import get_costs_of_detail_ids
# repositories
from repositories.degree_repository import degree_repository
from repositories.detail_codes_repository import detail_codes_repository
# utils
from utils.decoder import get_student_data


degree = APIBlueprint(
    'Degree',
    __name__,
    url_prefix=DEGREE_ROUTE,
    abp_tags=[Tag(name="Degree",
                  description="'Degree' procedure")],
    abp_responses={
        "400": BadRequest,
        "401": Unauthorized,
        "403": Forbidden,
        "404": NotFound,
        "503": UnavailableService
    }
)


@degree.get('', responses={"200": DegreResponseGet}, security=[{"jwt": []}])
def degree_get_controller(header: Headers):
    """
        Endpoint to request "Degree" procedure to salesforce
    """
    # AUTH_HEADER
    auth_header = req.headers[Authorization]
    student_data = get_student_data(auth_header)
    email = student_data.email
    school = student_data.school
    modality = student_data.modality
    logger.debug(f"{email} - Controller accessed.")

    # UPDATE COLLECTIONS IF NEEDED
    check_if_update_needed_in_degree_procedure_records(email, school, modality)

    # PERMISSIONS_PROGRAMS
    programs = get_programs_detail(email, auth_header)
    # Converting to the DICT
    items = degree_repository().find({"procedureType": degreeType, "modality": modality})
    items2 = items.clone()
    # get all_detail_codes
    all_detail_codes = get_all_detail_codes(email, school)
    # filter and get list detail codes only degree
    list_detail_codes = get_list_detail_codes(email, student_data, items, all_detail_codes)
    # get list costs
    list_costs = get_costs_of_detail_ids(email, auth_header, list_detail_codes)
    # get Flags degree
    flags_degree = degree_repository().find_one({"identifier": "flagsDegree", "school": school})
    # generate record types
    record_types_array = generate_record_types(email, items2, list_costs, student_data, all_detail_codes, programs, flags_degree)

    logger.debug(f"{email} - The generated record type structure is: : {record_types_array}")
    guides_and_steps = degree_repository().find_one({"identifier": "guidesAndSteps"})

    # SEND RESPONSE
    degree_response_data = {
        'recordType': record_types_array,
        'filesLinks': guides_and_steps["filesLinks"],
        'stepsGuideOnlineDegree': guides_and_steps["stepsGuideOnlineDegree"],
        'stepsGuideGraduateDegree': guides_and_steps["stepsGuideGraduateDegree"]
    }

    status_info = "RecordTypes, files links and steps guide degree sent"
    logger.info(f"{email} - {status_info}")

    return successful_response_get_method(degree_response_data, status_info)


@degree.post('', responses={"200": DegreResponsePost}, security=[{"jwt": []}])
def degree_post_controller(header: Headers, body: RequestBodyDegree):
    """
          Endpoint to request "Degree request post" procedure to salesforce
    """
    auth_header = req.headers['Authorization']
    student_data = get_student_data(auth_header)
    email = student_data.email
    school = student_data.school
    modality = student_data.modality
    logger.debug(f"{email} - Controller accessed.")
    properties = set_servicio_properties(student_data, body, degree.name, auth_header)
    logger.debug(f"{email} - Properties object: '{properties}")
    # SET SF REQUEST BODY # verificar y hacer cambio de "recordtype" para cambiar el record type
    sf_request_body = {
        "servicio": [properties],
        "files": req.json['files'],
        "matricula": properties["Matricula__c"],
        "recordtype": body.recordTypeId,
    }
    re_body = {"servicio": [properties], "matricula": properties["Matricula__c"], "recordtype": body.recordTypeId}

    logger.debug(f"{email} - data without files: {re_body}")

    # CONSUME PROCEDURES SERVICE TO REQUEST 'Titulación'
    procedure = 'Titulación'
    ticket_number = request_procedure_to_salesforce(
        student_data,
        procedure,
        sf_request_body
    )

    # CONSUME 'PAYMENTS' SERVICE TO RETRIEVE TRANSACTION NUMBER
    # FETCH DEGREE RECORD DETAIL CODE
    # get all_detail_codes
    all_detail_codes = get_all_detail_codes(email, school)
    detail_code: str = ''
    if modality == DISTANCIA or modality == ESCOLARIZADA:
        if body.paymentTypeValue:
            detail_code = fetch_degree_record_detail_code(student_data, body.paymentTypeValue, 1, all_detail_codes)
        if body.typeValue:
            detail_code = fetch_degree_record_detail_code(student_data, body.typeValue, 1, all_detail_codes)

    logger.debug(f"{email} - degree_record_detail_code:{detail_code}")

    transaction_number = get_transaction_number(
        student_data,
        auth_header,
        ticket_number,
        detail_code)
    logger.debug(f"{email} - transaction_number: {transaction_number}")
    return successful_response_post_method(email, ticket_number, transaction_number, procedure)
    