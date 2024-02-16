from pydantic import BaseModel, Field
from typing import Optional


class StudentData:
    enrollmentNumber: str
    name: str
    email: str
    phoneNumber: str
    campus: str
    program: str
    level: str
    levelCode: str
    modality: str
    studentId: int
    periodCode: str
    school: str
    cuatrimestre: str


class Servicio_UTC(BaseModel):
    Nombre_de_la_cuenta__c: str
    Correo_Institucional_UTC__c: str
    Matricula__c: str
    Campus_UTC__c: str
    Nivel_UTC__c: str
    Programa_UTC__c: str
    Modalidad_UTC__c: str
    Numero_de_telefono__c: str
    # Tipo_de_Entrega_UTC__c: str
    # Selecciona_Campus_UTC__c: str
    Comentarios__c: str = None
    Etapa_UTC__c: str = Field('Nuevo')
    Asignar_mediante_las_reglas__c: bool = Field(True)


class ServicioUtcWithCharge(Servicio_UTC):
    Acepto_el_Cargo__c: bool


class CommonsServicio_ULA(BaseModel):
    Nombre_de_la_cuenta__c: str
    Matricula__c: str
    Email_en_RFI__c: str
    Numero_de_telefono__c: str
    Campus_Banner__c: str
    Nivel_Banner__c: str
    Descripcion__c: str = None
    Programa_ONLINE_Banner__c: str
    Acepto_el_Cargo__c: bool
    Status__c: str = Field('Nuevo')
    Asignar_mediante_las_reglas__c: bool = Field(True)


class ServicioUlaAddedFields(CommonsServicio_ULA):

    Pa_s_de_Nacimiento__c: str
    Pa_s_de_Estudios_Inmediatos_Anteriores__c: str
    Nombre_Escuela_de_Procedencia__c: str

    Calle_EP__c: str
    N_mero_EP__c: str
    Colonia_EP__c: str
    C_P__c: str
    Poblaci_n__c: str
    Ciudad__c: str
    Entidad__c: str

    Tel_fono_Escuela_de_Procedencia__c: str
    Email_Escuela_de_Procedencia__c: str
    Fecha_Inicio_de_Bachillerato__c: str
    Fecha_Fin_Bachillerato__c: str


class SfRequestBody:
    servicio: list[Servicio_UTC]
    files: list
    matricula: str
    recordtype: str
