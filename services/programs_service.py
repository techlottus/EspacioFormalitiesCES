from collections import OrderedDict
from typing import Any, Hashable, Optional, Iterable

import requests
from datetime import date
# constants
from constants.identifiers_constants import PERMISSIONS_SERVICE_ID, ULA, ESCOLARIZADA
from constants.services_urls import PERMISSIONS_PROGRAMS_URL_ULA
# services
from services.logger_service import logger
from services.set_responses_service import error_response


def get_programs_detail(email: str, auth_header: str):
    logger.debug(f"{email} - get_programs() accessed")
    programs_array: []
    try:
        logger.info(f"Trying to get programs from 'permissions service' at {PERMISSIONS_PROGRAMS_URL_ULA}")

        headers = {
            'Authorization': 'Bearer ' + auth_header,
            'Service-Id': PERMISSIONS_SERVICE_ID
        }
        programs_response = requests.get(PERMISSIONS_PROGRAMS_URL_ULA, headers=headers)
        status_code = programs_response.status_code
        programs_response_json = programs_response.json()
        logger.debug(f"Programs service response: {programs_response_json}; status_code: {status_code}")
        programs_array = programs_response_json["data"]
        if programs_array:
            logger.info(f"Programs service answered correctly with programs array: {programs_array}")
        else:
            logger.error(f"Programs array couldn't be retrieved from 'permissions' service.")
            return error_response(503, "'permissions' service is not available")
    except Exception as e:
        logger.error(f"{email} - 'permissions' service is not available: {e}")
        return error_response(503, f"'permissions' service is not available: {e}")
    else:
        return programs_array


def format_programs(programs_array: [], prefix: str, student_data, flags_degree):
    format_programs_array = []
    checklist = set()

    for program in programs_array:
        if program["porcent"] <= 100.0:
            checklist.add(program["name"])

    for nameProgram in checklist:
        program = find_in_list_objects(programs_array, "name", nameProgram)
        program_formated = {
            'label': program["name"],
            'value': program["code"],
            # 'nivel': program["nivel"],
            # 'date': date.today(),
            "flags": get_flags(student_data, flags_degree, program["nivel"]),

        }
        format_programs_array.append(program_formated)

    return format_programs_array


def find_in_list_objects(it: Iterable[dict], clave: Hashable, valor: Any) -> Optional[dict]:
    for dicc in it:
        if dicc[clave] == valor:
            return dicc
    return None


def get_flags(student_data, flags_degree, level):
    global flags
    email = student_data.email
    school = student_data.school
    modality = student_data.modality


    if school == ULA:

        liberation_of_english = flags_degree["inputs"][0]
        liberation_of_social_service = flags_degree["inputs"][1]
        copy_of_bachelors_degree = flags_degree["inputs"][2]
        apostilled_title_for_foreigners = flags_degree["inputs"][3]
        copy_of_bachelors = flags_degree["inputs"][4]
        certificate_immigration_form = flags_degree["inputs"][5]

        flags = {
            "files": {
                "liberationOfEnglish": True if level in liberation_of_english["levels"] else False,
                "liberationOfSocialService": True if level in liberation_of_social_service["levels"] else False,
                "copyOfBachelorsDegree": True if level in copy_of_bachelors_degree["levels"] else False,
                "apostilledTitleForForeigners": False,
                "copyOfBachelors": True if level in copy_of_bachelors["levels"] else False,
                "certificateImmigrationForm": False,
            }
        }

    return flags

