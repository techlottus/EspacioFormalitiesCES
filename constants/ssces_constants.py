import os
from varname import nameof
from utils.utilities import log_not_defined_env_var

"""
SSCES constants
"""
HOST = '0.0.0.0'
PORT = os.getenv('PORT', 80)
SSCES = os.getenv("SSCES", "localhost")
SERVICE_ID = os.getenv('SERVICE_ID', "virtual-campus-ss-ces-api")
SERVICE_NAME = os.getenv('SERVICE_NAME', "SS-CES Service API")
ENVIRONMENT = os.getenv('ENVIRONMENT')

sscesResponse = {
    "service": {
        "id": SERVICE_ID,
        "name": SERVICE_NAME
    }
}

bad_request_error = {
    "error": {
                "id": 400,
                "name": "Bad Request",
                "message": ""
            }
}

URLDBREMOTE = os.getenv('URLDBREMOTE')
if URLDBREMOTE is None:
    log_not_defined_env_var(nameof(URLDBREMOTE))

MYDB = os.getenv('MYDB')
if MYDB is None:
    log_not_defined_env_var(nameof(MYDB))

PAYLOAD_LIMIT_SIZE = os.getenv("PAYLOAD_LIMIT_SIZE")
if PAYLOAD_LIMIT_SIZE is None:
    log_not_defined_env_var(nameof(PAYLOAD_LIMIT_SIZE))

MAX_LIMIT_SIZE = os.getenv("MAX_LIMIT_SIZE")
if MAX_LIMIT_SIZE is None:
    log_not_defined_env_var(nameof(MAX_LIMIT_SIZE))
