from pydantic import BaseModel, Field
from typing import Optional

from OpenAPI.commons import CommonRequestBody
from constants.ssces_constants import SERVICE_ID, SERVICE_NAME


class DegreResponsePost(BaseModel):
    data = {
        "ticketNumber": "12345678",
        "transactionNumber": "123456"
    }
    service = {
        "id": SERVICE_ID,
        "name": SERVICE_NAME
    }
    error = {}
    partialResponse = {}
    status = {
        "id": 200,
        "info": "'Degree' requested successfuly to Salesforce"
    }


class DegreResponseGet(BaseModel):
    data = {
        "recordType": [],
        "filesLinks": {},
        "stepsGuideOnlineDegree": [],
        "stepsGuideGraduateDegree": []
    }
    error = {}
    partialResponse = {}
    service = {
        "id": SERVICE_ID,
        "name": SERVICE_NAME
    }
    status = {
        "id": 200,
        "info": "Degree arrays sent"
    }


class RequestBodyDegree(CommonRequestBody):
    recordTypeId: str
    paymentTypeValue: Optional[str]
    programTypeValue: Optional[str]
    description: Optional[str]
    typeValue: Optional[str]
