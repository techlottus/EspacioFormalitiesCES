# database
from database.mongo.database import connection_db
# constants
from constants.ssces_constants import URLDBREMOTE, MYDB
from constants.collections_constants import DETAIL_CODES_COLLECTION_NAME


def detail_codes_repository():
    global repository
    connection = connection_db(URLDBREMOTE)
    if connection != "Communication_error":
        mydb = connection[str(MYDB)]
        repository = mydb[DETAIL_CODES_COLLECTION_NAME]

    return repository
