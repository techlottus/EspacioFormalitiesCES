from services.logger_service import logger
from repositories.degree_repository import degree_repository
from services.programs_service import get_programs_detail
from services.set_responses_service import error_response
from constants.identifiers_constants import DISTANCIA, ESCOLARIZADA


def get_record_type_id(record_type_name: str):
    logger.debug(f"Function get_record_type_id() accessed")
    record_type_document = fetch_record_type_document_by_name(record_type_name)
    record_type_id = record_type_document["recordTypeId"]
    logger.debug(f"record_type_id is: {record_type_id}")
    return record_type_id


def fetch_record_type_document_by_name(record_type_name: str):
    logger.debug(f"Function fetch_record_type_document_by_name() accessed")
    record_type_document = degree_repository().find_one({"name": record_type_name})
    if not record_type_document:
        logger.error(f"No record type found for name: '{record_type_name}")
        return error_response(404, "No record type found", "No record type found")
    logger.debug(f"the record_type is: {record_type_document}")
    return record_type_document


def get_record_type_name(record_type_id: str):
    logger.debug(f"Function get_record_type_name() accessed")
    record_type_document = fetch_record_type_document_by_id(record_type_id)
    record_type_name = record_type_document["name"]
    logger.debug(f"The record_type_name is: {record_type_name}")
    return record_type_name


def fetch_record_type_document_by_id(record_type_id: str, modality: str, name: str):
    logger.debug(f"Function fetch_record_type_document_by_id() accessed")
    filter_params = {"recordTypeId": record_type_id, "modality": modality, "name": name}
    logger.debug(f"Fetching record type document with params: {filter_params}")
    record_type_document = degree_repository().find_one(filter_params)
    logger.debug(f"record_type_document: {record_type_document}")
    if not record_type_document:
        logger.error(f"No record type found for recordTypeId: '{record_type_id}")
        return error_response(404, "No record type found", "No record type found")
    logger.debug(f"The record_type is: {record_type_document}")
    return record_type_document


def get_label_of_pick_list_request_type(record_type_id: str, type_value: str, modality: str, name: str):
    logger.debug(f"Function get_label_of_pick_list_request_type() accessed")
    record_type_document = fetch_record_type_document_by_id(record_type_id, modality, name)
    logger.debug(f"type_value is: {type_value}")
    logger.debug(f"record_type_document is: {record_type_document}")

    global items_array
    if modality == DISTANCIA:
        items_array = record_type_document["paymentType"]
    elif modality == ESCOLARIZADA:
        items_array = record_type_document["types"]

    try:
        type = list(filter(lambda item: item["value"] == type_value, items_array))
        label = type[0]["label"]
        logger.debug(f"Label  is: {label}")
        return label
    except Exception as e:
        no_type_found_err_message = f"No type found with value '{type_value}' for recordTypeId '{record_type_id}'," \
                                 f" '{record_type_document['name']}"
        return error_response(404, no_type_found_err_message, no_type_found_err_message)


def get_label_list_request_programs(email: str, auth_header, type_value: str):
    # PERMISSIONS_PROGRAMS
    logger.debug(f"Function get_label_list_request_programs() accessed")
    programs = get_programs_detail(email, auth_header)
    try:
        program = list(filter(lambda program: program["code"] == type_value, programs))
        label = program[0]["name"]
        logger.debug(f"Label is: {label}")
        return label
    except Exception as e:
        err_message = f"The program not found for value: {type_value}"
        return error_response(404, err_message, err_message)