from pydantic import BaseModel

from OpenAPI.commons import CommonRequestBody
from constants.ssces_constants import SERVICE_ID, SERVICE_NAME


class RevalidationResponse(BaseModel):
    service = {
        "id": SERVICE_ID,
        "name": SERVICE_NAME
    }
    status = {
        "id": 200,
        "info": "'Revalidation' requested successfully to Salesforce"
    }
    data = {
        "ticketNumber": "12345678",
        "transactionNumber": "123456"
    }


class RevalidationRequestBody(CommonRequestBody):
    countryOfBirth: str
    countryOfPriorStudies: str
    schoolOfOrigin: str

    street: str
    number: str
    neighborhood: str
    cp: str
    population: str
    city: str
    entity: str

    schoolPhone: str
    schoolEmail: str
    startDatePreviousLevel: str
    endDatePreviousLevel: str