# database
from database.mongo.database import connection_db
# constants
from constants.ssces_constants import URLDBREMOTE, MYDB


def scores_repository():
    global repository
    connection = connection_db(URLDBREMOTE)
    if connection != "Communication_error":
        mydb = connection[str(MYDB)]
        repository = mydb["ADS_Scores_Medallia"]

    return repository
