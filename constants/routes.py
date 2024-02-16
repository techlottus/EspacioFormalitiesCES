from constants.ssces_constants import SSCES, PORT
from services.logger_service import logger

SWAGGER_URL = '/openapi/swagger'
PREFIX = '/schoolServices-ces/api/'
CREDENTIAL_ROUTE = PREFIX + 'credential/v1'
DEGREE_ROUTE = PREFIX + 'degree/v1'
EQUIVALENCE_ROUTE = PREFIX + 'equivalencyOfStudies/v1'
REINSTATEMENT_ROUTE = PREFIX + 'reinstatement/v1'
REVALIDATION_ROUTE = PREFIX + 'v1/revalidation'
TICKETS_ROUTE = PREFIX + 'requestAllProcedures/v1'

if SSCES == 'localhost':
    base_url = "http://" + SSCES + ':' + str(PORT)
else:
    base_url = SSCES
    logger.debug(f"base_url: {base_url}")

SERVICE_URLS = [
    CREDENTIAL_ROUTE,
    DEGREE_ROUTE,
    EQUIVALENCE_ROUTE,
    REINSTATEMENT_ROUTE,
    REVALIDATION_ROUTE,
    TICKETS_ROUTE,
]
