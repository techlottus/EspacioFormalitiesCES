# services
from constants.identifiers_constants import DISTANCIA, ESCOLARIZADA
from services.logger_service import logger
from services.sf_core_service import get_sf_access_token
# constants
from constants.degree_constants import degreeType, GRADUATEDEGREE_NAME, ONLINEDEGREE_NAME, TRADITIONALDEGREE_NAME
from constants.identifiers_constants import TIPO_DE_TITULACION_TRAD, TIPO_DE_PAGO_WA_ONLINE
from constants.collections_constants import RECORD_TYPES_COLLECTION_DEGREE_NAME
# Utilities
from utils.utilities import check_date_changed, create_id_with_prefix
from datetime import datetime
# repository's
from repositories.degree_repository import degree_repository
# services
from services.degree_record_types_service import get_record_type_id
from services.salesforce_requests_service import fetch_picklist
from services.set_responses_service import error_response

_record_types_repository = degree_repository()


def check_if_update_needed_in_degree_procedure_records(email: str, school: str, modality: str):
    """
        function to update collections of degree
    """
    logger.debug(f"{email} - {check_if_update_needed_in_degree_procedure_records.__name__}() accessed.")

    degree_procedure_records_need_update = check_update_in_types_arrays(email, degreeType, modality)
    if degree_procedure_records_need_update:
        # TO GET ACCESS-TOKEN OF SALES FORCE
        access_token = get_sf_access_token(email, school)
        if modality == DISTANCIA:
            update_record_types_collection(email, access_token, ONLINEDEGREE_NAME, TIPO_DE_PAGO_WA_ONLINE, modality)
            update_record_types_collection(email, access_token, GRADUATEDEGREE_NAME, TIPO_DE_PAGO_WA_ONLINE, modality)

        if modality == ESCOLARIZADA:
            update_record_types_collection(email, access_token, ONLINEDEGREE_NAME, TIPO_DE_TITULACION_TRAD, modality)
            update_record_types_collection(email, access_token, GRADUATEDEGREE_NAME, TIPO_DE_TITULACION_TRAD, modality)


def check_update_in_types_arrays(email: str, procedure_type: str, modality: str):
    logger.debug(f"{email} - check_update_in_types_arrays() accessed")
    item = _record_types_repository.find_one({"procedureType": procedure_type, "modality": modality})
    update_needed: bool

    if item is None:
        logger.warn(f"{email} - There are no records with help type name {procedure_type}")
        update_needed = True
    else:
        # get date of item
        if item["paymentType"]:
            aDate = str(item["paymentType"][0]['date']).split(":")[0]
        elif item["types"]:
            aDate = str(item["types"][0]['date']).split(":")[0]
        aDate = aDate.split(" ")
        aDate = aDate[0].split("-")
        last_update_date = datetime(int(aDate[0]), int(aDate[1]), int(aDate[2]))
        if not last_update_date:
            update_needed = True
        else:
            update_needed = check_date_changed(last_update_date)

        if update_needed:
            logger.debug(f"{email} - Records of '{procedure_type}' with modality '{modality}' need to be updated")
            return True
        else:
            logger.debug(f"{email} - Records of '{procedure_type}' with modality '{modality}' don't need to be updated")
            return False


def update_record_types_collection(
        email: str,
        access_token: str,
        record_type_name: str,
        type_pick_list: str,
        modality: str
):
    logger.debug(f"{email} - {update_record_types_collection.__name__}() accessed")

    types_array_with_date = fetch_pick_list_and_return_array_with_date(
        email,
        record_type_name,
        access_token,
        type_pick_list
    )

    logger.debug(f"{email} - record_type_name: {record_type_name}")
    logger.debug(f"{email} - types_array_with_date: {types_array_with_date}")

    record_type_document = _record_types_repository.find_one({"name": record_type_name, "modality": modality})

    if not record_type_document:
        logger.error(f"{record_type_name}' was not found in '{RECORD_TYPES_COLLECTION_DEGREE_NAME}' collection")
        return error_response(404, "Record type name not found", "Record type name not found"), 404

    if types_array_with_date.__class__ == tuple:
        logger.debug(f' There was an error {types_array_with_date[0]["error"]["info"] } the collection was not updated.')
    else:

        updated_record_type = {
            "_id": record_type_document["_id"],
            "name": record_type_document["name"],
            "procedureType": record_type_document["procedureType"],
            "description": record_type_document["description"],
            "recordTypeId": record_type_document["recordTypeId"],
            "label": record_type_document["label"],
            "acrom": record_type_document["acrom"],
            "modality": record_type_document["modality"],
        }

        if type_pick_list == TIPO_DE_PAGO_WA_ONLINE:
            updated_record_type["paymentType"] = types_array_with_date
        elif type_pick_list == TIPO_DE_TITULACION_TRAD:
            updated_record_type["types"] = types_array_with_date

        _record_types_repository.update_one({"name": record_type_name, "modality": modality}, {"$set": updated_record_type})
        logger.debug(f"{record_type_name}' record for '{RECORD_TYPES_COLLECTION_DEGREE_NAME}' collection updated.")


def fetch_pick_list_and_return_array_with_date(
        email: str,
        record_type_name: str,
        sf_auth_header: str,
        pick_list_name: str
):
    logger.debug(f"{email} - {fetch_pick_list_and_return_array_with_date.__name__}() accessed")

    pick_list_array = fetch_picklist(email, pick_list_name, record_type_name, sf_auth_header)
    pick_list_array_with_date = []

    if len(pick_list_array) != 0:
        for item in pick_list_array:
            item_object = {
                "label": item["Label"],
                "value": create_id_with_prefix(record_type_name, item["Label"]),
                "date": datetime.now(),
            }
            pick_list_array_with_date.append(item_object)
    else:
        # Only query what is in the database when the array is empty
        logger.debug(f"{email} - The data from pick_list_array it is empty, but the backup data is consulted of DB")
        data_in_mongo = list(_record_types_repository.find({"name": record_type_name}))
        pick_list_array_with_date = data_in_mongo[0]['paymentType']
        logger.debug(f"{email} - backup data database is: {pick_list_array_with_date}")
    return pick_list_array_with_date
