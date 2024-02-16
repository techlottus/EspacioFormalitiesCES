from pydantic import BaseModel
from constants.ssces_constants import SERVICE_ID, SERVICE_NAME


class EquivalenceStudiesResponse(BaseModel):
    service = {
        "id": SERVICE_ID,
        "name": SERVICE_NAME
    }
    status = {
        "id": 200,
        "info": "'Equivalencia de Estudios' requested successfuly to Salesforce"
    }
    error = {}
    data = {
        "ticketNumber": "12345678",
        "transactionNumber": "123456"
    }
    partialResponse = {}
