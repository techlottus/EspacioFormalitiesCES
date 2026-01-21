# database
from database.mongo.database import connection_db
# constants
from constants.ssces_constants import URLDBREMOTE, MYDB
from constants.collections_constants import SCHOLARSHIP_DOCUMENTS_NAME


def scholarship_documents_repository():
    connection = connection_db(URLDBREMOTE)
    if connection != "Communication_error":
        mydb = connection[str(MYDB)]
        repository = mydb[SCHOLARSHIP_DOCUMENTS_NAME]
        return repository
