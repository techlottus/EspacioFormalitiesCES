from pydantic import BaseModel
from constants.ssces_constants import SERVICE_ID, SERVICE_NAME
from OpenAPI.commons import CommonRequestBody


class ReinstatementResponse(BaseModel):
    service = {
        "id": SERVICE_ID,
        "name": SERVICE_NAME
    }
    status = {
        "id": 200,
        "info": "'Reinstatement' requested successfully to Salesforce"
    }
    data = {
        "ticketNumber": "12345678",
        "transactionNumber": "123456"
    }

