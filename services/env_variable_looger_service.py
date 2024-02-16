import os
import datetime as dt
from database.mongo.database import connection_db
from constants.ssces_constants import ENVIRONMENT, URLDBREMOTE, MYDB
from utils.utilities import log_not_defined_env_var

mongo = connection_db(URLDBREMOTE)
mydb = mongo[str(MYDB)]
BackLogs = mydb["BackLogs"]


def log_mongo_not_defined_var(var_name: str):
    log_not_defined_env_var(var_name)
    BackLogs.insert_one({
        "service": "SSCES",
        "description": f"Variable {var_name} is not defined,",
        "variable": var_name,
        "date": str(dt.datetime.now().strftime('%Y-%m-%d')),
        "time": str(dt.datetime.now().strftime('%H:%M:%S %p')),
        "environment": ENVIRONMENT
    })


