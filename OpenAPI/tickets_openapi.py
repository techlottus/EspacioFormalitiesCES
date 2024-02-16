from pydantic import BaseModel
from constants.ssces_constants import SERVICE_ID, SERVICE_NAME


class TicketsArray(BaseModel):
    alumno: str
    estatus: str
    subestatus: str
    servicio: str
    programa: str
    matricula: str
    numticket: str
    fechasolicitud: str


class TicketsResponse(BaseModel):
    service = {
        "id": SERVICE_ID,
        "name": SERVICE_NAME
    }
    status = {
        "id": 200,
        "info": "Tickets array sent"
    }
    error = {}
    data: list[TicketsArray]
    partialResponse = {}
