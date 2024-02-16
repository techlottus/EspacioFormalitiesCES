import pymongo
import pymongo.errors
from services.logger_service import logger


def connection_db(url):
    """
        this function makes the connection to MongoDB
        :return: the connection
    """
    # connection basic
    try:
        connection = pymongo.MongoClient(url)
        # logger.debug(f"Connection to: {connection}.")

        logger.info("Connection with remote Mongo database was successful")
        return connection
    except pymongo.errors.ConnectionFailure as e:
        logger.error(f'Could not connect to server: {e}')
        logger.error("An error occurred while trying to communicate with the mongodb database")
        return "Communication_error"
