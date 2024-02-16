import os
from varname import nameof
from services.env_variable_looger_service import log_mongo_not_defined_var

"""
Services URL constants
"""

# URLS
OAUTH_URL = os.getenv('OAUTH_SERVICE_URL')
if OAUTH_URL is None:
    log_mongo_not_defined_var(nameof(OAUTH_URL))

SF_CORE_URL = os.getenv('SF_CORE_URL')
if SF_CORE_URL is None:
    log_mongo_not_defined_var(nameof(SF_CORE_URL))

SF_PICKLIST_URL_UTC = os.getenv('SF_PICKLIST_URL_UTC')
if SF_PICKLIST_URL_UTC is None:
    log_mongo_not_defined_var(nameof(SF_PICKLIST_URL_UTC))

SF_PICKLIST_URL_ULA = os.getenv('SF_PICKLIST_URL_ULA')
if SF_PICKLIST_URL_ULA is None:
    log_mongo_not_defined_var(nameof(SF_PICKLIST_URL_ULA))

SF_SERVICIOS_ESCOLARES_URL_UTC = os.getenv('SF_SERVICIOS_ESCOLARES_URL_UTC')
SF_REQUEST_TICKETS_URL_UTC = ''
if SF_SERVICIOS_ESCOLARES_URL_UTC is None:
    log_mongo_not_defined_var(nameof(SF_SERVICIOS_ESCOLARES_URL_UTC))
else:
    SF_REQUEST_TICKETS_URL_UTC = SF_SERVICIOS_ESCOLARES_URL_UTC + "?matricula="

SF_SERVICIOS_ESCOLARES_URL_ULA = os.getenv('SF_SERVICIOS_ESCOLARES_URL_ULA')
SF_REQUEST_TICKETS_URL_ULA = ''
if SF_SERVICIOS_ESCOLARES_URL_ULA is None:
    log_mongo_not_defined_var(nameof(SF_SERVICIOS_ESCOLARES_URL_ULA))
else:
    SF_REQUEST_TICKETS_URL_ULA = SF_SERVICIOS_ESCOLARES_URL_ULA + "?matricula="

PAYMENTS_ADD_TRANSACTION_URL = os.getenv("PAYMENTS_ADD_TRANSACTION_URL")
if PAYMENTS_ADD_TRANSACTION_URL is None:
    log_mongo_not_defined_var(nameof(PAYMENTS_ADD_TRANSACTION_URL))

PAYMENTS_GET_TRANSACTION_URL = os.getenv("PAYMENTS_GET_TRANSACTION_URL")
if PAYMENTS_GET_TRANSACTION_URL is None:
    log_mongo_not_defined_var(nameof(PAYMENTS_GET_TRANSACTION_URL))

COSTS_SERVICE_URL = os.getenv("COSTS_SERVICE_URL")
if COSTS_SERVICE_URL is None:
    log_mongo_not_defined_var(nameof(COSTS_SERVICE_URL))

PERMISSIONS_PROGRAMS_URL_ULA = os.getenv("PERMISSIONS_PROGRAMS_URL_ULA")
if PERMISSIONS_PROGRAMS_URL_ULA is None:
    log_mongo_not_defined_var(nameof(PERMISSIONS_PROGRAMS_URL_ULA))
