# python modules
from flask_openapi3 import APIBlueprint, Tag
from flask import current_app
import requests
import copy
import datetime as dt
# OpenAPI
from OpenAPI.commons import *
from OpenAPI.credential_openapi import CredentialResponse
# services
from services.logger_service import logger
# constants
from constants.ssces_constants import sscesResponse
from constants.routes import CREDENTIAL_ROUTE
from constants.services_urls import SF_CORE_URL, SF_PICKLIST_URL_UTC
# utils
from utils.functions import functions

# object utils
fun = functions()

credential = APIBlueprint(
    'credential',
    __name__,
    url_prefix=CREDENTIAL_ROUTE,
    abp_tags=[Tag(name="credential", description="Credential comobos")],
    abp_responses={
        "400": BadRequest,
        "401": Unauthorized,
        "403": Forbidden,
    }
)


@credential.get('', responses={"200": CredentialResponse}, security=[{"jwt": []}])
def get_credentials(header: Headers):
    """
    Return array of campus, and credentials type
    """
    logger.debug("controller accessed.")
    # connection to database mongo
    logger.debug("Conection to database mongo")
    mongodb = current_app.config["mondoDB"]

    #response sales force
    logger.debug("Obtaining access token SF")
    sf_core_response = requests.get(SF_CORE_URL).json()
    logger.debug(f"Sales force core response: {sf_core_response}")
    access_token = sf_core_response['sfData']['accessToken']

    #response picklist crednetial
    params= { "namePickList": "Tipo_de_Solicitud_de_Credencial_UTC__c"}
    token_header = {'Authorization': 'Bearer ' + access_token}
    sf_credential_response = requests.get(SF_PICKLIST_URL_UTC, params=params, headers=token_header).json()
    logger.debug(f"Sales force core response,  credential: {sf_credential_response}")

    # verification of date now vs date of the document saved
    verification = fun.verificatedDateOfcollection(dt.datetime.now(), mongodb.db.Campus.find()[1])
    logger.debug(f"Verification current date versus document date: {verification}")

    listcampusTmp = []
    if verification != True:
        logger.debug("Case of verification of date is Fasle, not identical date")
        # response sales force
        sf_core_response = requests.get(SF_CORE_URL).json()
        logger.debug(f"Sales force core response: {sf_core_response}")
        access_token = sf_core_response['sfData']['accessToken']
        logger.debug("Obtaining access token SF")

        # response picklist campus
        params= { "namePickList": "Selecciona_Campus_UTC__c"}
        token_header = {'Authorization': 'Bearer ' + access_token}
        sf_campus_response = requests.get(SF_PICKLIST_URL_UTC, params=params, headers=token_header)
        logger.debug(f"Sales force core response: {sf_campus_response}")
        # create list of campus with date upgrated
        listcampusTmp = fun.createList(sf_campus_response)
        logger.debug(f"Create list of campus to save: {listcampusTmp}")

        # save in database new list of campus with date  upgrated
        mongodb.db.Campus.delete_many({})
        logger.debug(f"Clean to collection of campus in database with new date")
        for campus in listcampusTmp:
            # save document in colection
            mongodb.db.Campus.insert_one({"label": campus['label'],
                                          "value": campus['Value'],
                                          "date": str(dt.datetime.now().strftime('%Y-%m-%d'))}
                                         )
    else:
        logger.debug("Case of verification of date is True, identical date")
        campus = mongodb.db.Campus.find()
        logger.debug("Find collection campus in database and add to object of campus")
        for campo in campus:
            obj = {"label": campo['label'], "Value": campo['value']}
            listcampusTmp.append(obj)
            obj = {}

    # SET RESPONSE
    logger.debug("Create response of the request")
    logger.debug(f"listcampusTemp: {listcampusTmp}")
    credential_response = copy.deepcopy(sscesResponse)
    credential_response['data']['campus'] = listcampusTmp
    credential_response['data']['credentialRequestType'] = sf_credential_response
    credential_response['data']['credentialType'] = [{"label": "Credencial Física", "value": 1},
                                            {"label": "Credencial Digital", "value": 2}]
    credential_response['status']['id'] = 200
    credential_response['status']['info'] = "Credentials info sent"

    logger.info("SSCES answered correctly with campus array")
    return credential_response, 200


@credential.route('', methods=['POST'])
def request_credential():
    """
    Request credential to salesforce
    """
    # 1.-create token accesa
    url="https://app-cv-oauth-dev.azurewebsites.net/createTokens"
    response = requests.post(url)
    print(response.content)
    payload = response.json()

    #print(payload)

    print("--------------------------------------")
    print(payload['accessToken'])

    payload = fun.validate_token(payload['accessToken'], 'f14846ead3374b523413334917333d98')

    print(payload)

    # 2.-verificated token
    """
    headers = {
        "Authorization": "Bearer " + payload['accessToken'],
        'Content-Type': 'application/json'
    }
    url2 = "https://app-cv-oauth-dev.azurewebsites.net/checkAuthorization"
    response2 = requests.get(url2,headers = headers)
    print(response2.text)
    print(response2.content)
    print(response2.headers)
    print(response2.json())
    print(response2)
    """









