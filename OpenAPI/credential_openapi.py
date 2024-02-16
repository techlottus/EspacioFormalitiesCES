from pydantic import BaseModel
from constants.ssces_constants import SERVICE_ID, SERVICE_NAME


class Campus(BaseModel):
    label: str
    value: int


class ContentData(BaseModel):
    campus: list[Campus]


class CredentialResponse(BaseModel):
    service = {
        "id": SERVICE_ID,
        "name": SERVICE_NAME
    }
    status = {
        "id": 200,
        "info": "Credentials data sent"
    }
    error = {}
    data: ContentData
    partialResponse = {}
