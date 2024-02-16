# database
from database.mongo.database import connection_db
# constants
from constants.ssces_constants import URLDBREMOTE, MYDB
from constants.collections_constants import KEYS_COLLECTION_NAME


def keys_repository():
    connection = connection_db(URLDBREMOTE)
    if connection != "Communication_error":
        mydb = connection[str(MYDB)]
        repository = mydb[KEYS_COLLECTION_NAME]
        return repository
