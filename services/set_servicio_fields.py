# Open API
from OpenAPI.commons import CommonRequestBody
# services
from OpenAPI.revalidation_openapi import RevalidationRequestBody
from constants.degree_constants import ONLINEDEGREE_NAME, GRADUATEDEGREE_NAME
from constants.identifiers_constants import UTC, ULA, DISTANCIA, ESCOLARIZADA
from constants.messages import unavailable_option
from interfaces.interfaces import StudentData, Servicio_UTC, ServicioUtcWithCharge, CommonsServicio_ULA, \
    ServicioUlaAddedFields
from services.degree_record_types_service import get_label_of_pick_list_request_type, get_label_list_request_programs
from services.logger_service import logger
from services.set_responses_service import error_response
from utils.utilities import set_sf_date_format


def set_servicio_properties(
        student_data: StudentData,
        body,
        service_name: str,
        auth_header: str = None
):
    """
    Sets servicio_object properties
    """

    email = student_data.email
    logger.debug(f"{email} - {set_servicio_properties.__name__}() accessed")

    school = student_data.school
    if school == UTC:
        return set_servicio_utc_with_charge(student_data, body)
    elif school == ULA:
        if service_name == "equivalence_of_studies":
            return set_commons_servicio_properties_ula(student_data, body)
        elif service_name == "Revalidation":
            return set_revalidation_fields(student_data, body)
        elif service_name == "Degree":
            return set_degree_fields(student_data, body, auth_header)
    else:
        return error_response(404, f"There is no such option: {school}", unavailable_option), 404


def set_commons_servicio_properties_utc(student_data: StudentData, body: CommonRequestBody):
    email = student_data.email
    logger.debug(f'{email} - Function set_commons_servicio_properties_utc() accessed')
    service_object = {
        "Nombre_de_la_cuenta__c": student_data.name,
        "Correo_Institucional_UTC__c": email,
        "Matricula__c": student_data.enrollmentNumber,
        "Campus_UTC__c": student_data.campus,
        "Nivel_UTC__c": student_data.level,
        "Programa_UTC__c": student_data.program,
        "Modalidad_UTC__c": student_data.modality,
        "Numero_de_telefono__c": student_data.phoneNumber,
        "Comentarios__c": body.comments
    }

    service_object = Servicio_UTC.parse_obj(service_object)
    if body.phoneNumber is not None:
        service_object.Numero_de_telefono__c = body.phoneNumber
    return service_object


def set_servicio_utc_with_charge(student_data: StudentData, body: CommonRequestBody):
    email = student_data.email
    logger.debug(f'{email} - Function set_servicio_utc_with_charge() accessed')
    service_object = set_commons_servicio_properties_utc(student_data, body)
    service_object = service_object.__dict__
    service_object['Acepto_el_Cargo__c'] = body.chargeAccepted
    service_object = ServicioUtcWithCharge.parse_obj(service_object)
    logger.debug(f"{email} - Servicio object setted: {service_object.__dict__}")
    return service_object


def set_commons_servicio_properties_ula(student_data: StudentData, body: CommonRequestBody):
    email = student_data.email
    logger.debug(f'{email} - Function set_commons_servicio_properties_ula() accessed')
    service_fields = {
        "Matricula__c": student_data.enrollmentNumber,
        "Nombre_de_la_cuenta__c": student_data.name,
        "Email_en_RFI__c": email,
        "Numero_de_telefono__c": student_data.phoneNumber,

        "Campus_Banner__c": student_data.campus,
        "Programa_ONLINE_Banner__c": student_data.program,
        "Acepto_el_Cargo__c": body.chargeAccepted,
        "Descripcion__c": body.comments,

        "Nivel_Banner__c": student_data.level,

    }
    service_fields = CommonsServicio_ULA.parse_obj(service_fields)
    if body.phoneNumber is not None:
        service_fields.Numero_de_telefono__c = body.phoneNumber
    logger.debug(f"{email} - Servicio object setted: {service_fields.__dict__}")
    return service_fields


def set_revalidation_fields(student_data: StudentData, body: RevalidationRequestBody):
    email = student_data.email
    school = student_data.school
    logger.debug(f'{email} - Function set_servicio_ula_added_fields() accessed')
    service_object = set_commons_servicio_properties_ula(student_data, body)
    service_object = service_object.__dict__

    if body.countryOfBirth is not None:
        service_object['Pa_s_de_Nacimiento__c'] = body.countryOfBirth

    if body.countryOfPriorStudies is not None:
        service_object['Pa_s_de_Estudios_Inmediatos_Anteriores__c'] = body.countryOfPriorStudies

    if body.schoolOfOrigin is not None:
        service_object['Nombre_Escuela_de_Procedencia__c'] = body.schoolOfOrigin

    if body.street is not None:
        service_object['Calle_EP__c'] = body.street

    if body.number is not None:
        service_object['N_mero_EP__c'] = body.number

    if body.neighborhood is not None:
        service_object['Colonia_EP__c'] = body.neighborhood

    if body.cp is not None:
        service_object['C_P__c'] = body.cp

    if body.population is not None:
        service_object['Poblaci_n__c'] = body.population

    if body.city is not None:
        service_object['Ciudad__c'] = body.city

    if body.entity is not None:
        service_object['Entidad__c'] = body.entity

    if body.schoolPhone is not None:
        service_object['Tel_fono_Escuela_de_Procedencia__c'] = body.schoolPhone

    if body.schoolEmail is not None:
        service_object['Email_Escuela_de_Procedencia__c'] = body.schoolEmail

    if body.startDatePreviousLevel is not None:
        service_object['Fecha_Inicio_de_Bachillerato__c'] = set_sf_date_format(body.startDatePreviousLevel)

    if body.endDatePreviousLevel is not None:
        service_object['Fecha_Fin_Bachillerato__c'] = set_sf_date_format(body.endDatePreviousLevel)

    if school == "ULA":
        service_object = ServicioUlaAddedFields.parse_obj(service_object)
        logger.debug(f"{email} - Servicio object setted: {service_object.__dict__}")

    return service_object


def set_degree_fields(student_data: StudentData, body, auth_header):
    email = student_data.email
    logger.debug(f'{email} - {set_degree_fields.__name__} accessed')
    service_object = set_commons_servicio_properties_ula(student_data, body)
    service_object = service_object.__dict__

    logger.debug(f"{email} - modality: {student_data.modality}")
    if student_data.modality == DISTANCIA:
        del service_object["Descripcion__c"]
        del service_object["Nivel_Banner__c"]
        logger.debug(f"{email} - params to pick_list_request are: "
                     f"{body.recordTypeId, body.paymentTypeValue, student_data.modality} ")
        name_picklist = ONLINEDEGREE_NAME if body.paymentTypeValue[:3] == "ONL" else GRADUATEDEGREE_NAME
        service_object["Tipo_de_Pago_WA_ONLINE__c"] = get_label_of_pick_list_request_type(body.recordTypeId,
                                                                                          body.paymentTypeValue,
                                                                                          student_data.modality,
                                                                                          name_picklist)
        if body.programTypeValue is not None:
            label = get_label_list_request_programs(email, auth_header, body.programTypeValue),
            service_object["programa_a_titularse__c"] = label[0]

    elif student_data.modality == ESCOLARIZADA:
        if body.typeValue is not None:
            logger.debug(
                f"{email} - params to pick_list_request are:  {body.recordTypeId, body.typeValue, student_data.modality}")
            name_picklist = ONLINEDEGREE_NAME if body.typeValue[:3] == "ONL" else GRADUATEDEGREE_NAME
            service_object["Tipos_de_Titulacion_TRAD__c"] = get_label_of_pick_list_request_type(
                body.recordTypeId,
                body.typeValue,
                student_data.modality,
                name_picklist,
            )
        if body.programTypeValue is not None:
            label = get_label_list_request_programs(email, auth_header, body.programTypeValue),
            service_object["programa_a_titularse__c"] = label[0]

        if body.description is not None:
            service_object["Descripcion__c"] = body.description

    logger.debug(f"The service_object is: {service_object}")
    return service_object