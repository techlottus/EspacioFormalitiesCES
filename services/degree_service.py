# services
from constants.identifiers_constants import ULA, ESCOLARIZADA
from interfaces.interfaces import StudentData
from services.logger_service import logger
from services.programs_service import format_programs, get_flags
from services.set_responses_service import error_response
# constants
from constants.degree_constants import DEGREE_RECORD_1, DEGREE_RECORD_3, DEGREE_RECORD_6, DEGREE_RECORD_9, \
    DEGREE_RECORD_12, DEGREE_DIRECT, DEGREE_THEORETICAL_PRACTICAL, \
    DEGREE_CENEVAL, DEGREE_THESIS, DEGREE_SEMINARY, DEGREE_POSTGRADUATE
# repositories
from repositories.detail_codes_repository import detail_codes_repository
from repositories.degree_repository import degree_repository

_detail_codes_repository = detail_codes_repository()


def fetch_degree_record_detail_code(student_data: StudentData, body_type_value: str, select_log, all_detail_codes):
    email = student_data.email
    school = student_data.school
    if select_log == 1:
        logger.debug(f"{email} - fetch_degree_record_detail_code() accessed")

    procedure: str = ''
    if body_type_value == "ONL11S4E10" or body_type_value == "GRA11S4E10":
        procedure = DEGREE_RECORD_1
    if body_type_value == "ONL31M13" or body_type_value == "GRA31M13":
        procedure = DEGREE_RECORD_3
    if body_type_value == "ONL61M13" or body_type_value == "GRA61M13":
        procedure = DEGREE_RECORD_6
    if body_type_value == "ONL91M13" or body_type_value == "GRA91M13":
        procedure = DEGREE_RECORD_9
    if body_type_value == "ONL12M13" or body_type_value == "GRA12M13":
        procedure = DEGREE_RECORD_12

    if body_type_value == "ONLT10D7" or body_type_value == "GRAT10D7":
        procedure = DEGREE_DIRECT
    if body_type_value == "ONLE6G7D2C12T7Y1P8" or body_type_value == "GRAE6G7D2C12T7Y1P8":
        procedure = DEGREE_THEORETICAL_PRACTICAL
    if body_type_value == "ONLC7" or body_type_value == "GRAC7":
        procedure = DEGREE_CENEVAL
    if body_type_value == "ONLT5" or body_type_value == "GRAT5":
        procedure = DEGREE_THESIS
    if body_type_value == "ONLS9" or body_type_value == "GRAS9":
        procedure = DEGREE_SEMINARY
    if body_type_value == "ONLP8" or body_type_value == "GRAP8":
        procedure = DEGREE_POSTGRADUATE

    if select_log == 1:
        logger.debug(f"{email} - payment_type_value: {body_type_value}")
        logger.debug(f"{email} - school: {school}")
        # logger.debug(f"{email} - detail code: {degree_record_document['detailCode']}")
    obj_code = list(filter(lambda code: code['procedure'] == procedure, all_detail_codes))
    degree_record_detail_code = obj_code[0]['detailCode']

    return degree_record_detail_code


def get_list_detail_codes(email, student_data, items, all_detail_codes):
    logger.debug(f"{email} - get_list_detail_codes() accessed.")
    list_detail_codes = set()

    for item in items:
        # FETCH DETAIL CODES OF COLLECTION
        if item["paymentType"]:
            list_detail_codes = map(
                lambda paymentType: fetch_degree_record_detail_code(student_data, paymentType["value"], 1,
                                                                    all_detail_codes), item["paymentType"])
        if item["types"]:
            list_detail_codes = map(
                lambda types: fetch_degree_record_detail_code(student_data, types["value"], 1,
                                                              all_detail_codes), item["types"])

    list_codes = list(list_detail_codes)
    logger.debug(f"{email} - The detail codes for the items are: {list_codes} for modality: {student_data.modality}")
    return list_codes


def get_cost(email, list_costs, degree_record_detail_code):
    # logger.debug(f"{email} - get_cost() accessed.")
    cost = list(filter(lambda cost: cost["codeDetail"] == degree_record_detail_code, list_costs))
    return cost


def get_all_detail_codes(email, school):
    logger.debug(f"{email} - get_all_detail_codes() accessed.")
    all_detail_codes = []
    try:
        all_detail_codes = list(_detail_codes_repository.find({"school": school, "service": "degree"}))
        logger.debug(f"{email} - the detail codes for the school: {school} are {all_detail_codes}")
    except Exception as e:
        return error_response(503, f"There was an error querying the database: {e}",
                              f"There was an error querying the database: {e}"), 503
    return all_detail_codes


def generate_record_types(email, items, list_costs, student_data, all_detail_codes, programs, flags_degree):
    logger.debug(f"{email} - generate_record_type() accessed.")
    global obj
    record_types_array = []
    for item in items:
        if item["paymentType"]:  # only Online
            for paymentType in item["paymentType"]:
                degree_record_detail_code = fetch_degree_record_detail_code(student_data, paymentType["value"], 0,
                                                                            all_detail_codes)
                obj_cost = get_cost(email, list_costs, degree_record_detail_code)
                paymentType["cost"] = obj_cost[0]["cost"]

                obj = {
                    "name": item["name"], "recordTypeId": item["recordTypeId"], "description": item["description"],
                    "paymentType": item["paymentType"], "label": item["label"], "acrom": item["acrom"],
                    "types": item["types"],
                    "programs": [] if item["name"] != "graduateDegree" else format_programs(programs, item["name"],
                                                                                            student_data, flags_degree),
                    "flags": get_flags(student_data, flags_degree,
                                       student_data.levelCode) if item["name"] == "onlineDegree" else {}
                }

            record_types_array.append(obj)

        if item["types"]:  # Only Escolarizada
            for type in item["types"]:
                degree_record_detail_code = fetch_degree_record_detail_code(student_data, type["value"], 0,
                                                                            all_detail_codes)
                obj_cost = get_cost(email, list_costs, degree_record_detail_code)
                type["cost"] = obj_cost[0]["cost"]

                obj = {
                    "name": item["name"], "recordTypeId": item["recordTypeId"], "description": item["description"],
                    "paymentType": item["paymentType"], "label": item["label"], "acrom": item["acrom"],
                    "types": item["types"],
                    "programs": [] if item["name"] != "graduateDegree" else format_programs(programs, item["name"],
                                                                                            student_data, flags_degree),
                    "flags": get_flags(student_data, flags_degree,
                                       student_data.levelCode) if item["name"] == "onlineDegree" else {}
                }

            record_types_array.append(obj)

    return record_types_array
