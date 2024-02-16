from app import create_app
from services.authorization_service import Authorization
from tests.commons import *

'''
def test_get_request_all_procedures_200(headers_with_data_online_utc, test_client):
    """
       GIVEN the headers from the request and
       WHEN authentication is verified
       THEN check the data of user, and return the Tickets array
    """
    responsec = test_client.get("/schoolServices-ces/api/requestAllProcedures/v1",
                                headers=headers_with_data_online_utc)

    assert responsec.status_code == 200


def test_get_request_all_procedures_data_online_ula_200(headers_with_data_online_ula, test_client):
    """
       GIVEN the headers from the request and
       WHEN authentication is verified
       THEN check the data of user, and return the Tickets array
    """
    responsec = test_client.get("/schoolServices-ces/api/requestAllProcedures/v1",
                                headers=headers_with_data_online_ula)

    assert responsec.status_code == 200



def test_get_request_all_procedures_data_schooled_ula_200(headers_with_data_schooled_ula, test_client):
    """
       GIVEN the headers from the request and
       WHEN authentication is verified
       THEN check the data of user, and return the Tickets array
    """
    responsec = test_client.get("/schoolServices-ces/api/requestAllProcedures/v1",
                                headers=headers_with_data_schooled_ula)

    assert responsec.status_code == 200
'''


def test_get_request_all_procedures_auth_invalid_401(header_auth_invalid, test_client):
    """
        GIVEN the headers from the request and
        WHEN authentication is verified, but the authorization is not a correct token
        THEN return a response with status 401 that the token is invalid
    """

    responsec = test_client.get("/schoolServices-ces/api/requestAllProcedures/v1", headers=header_auth_invalid)
    assert responsec.status_code == 401


def test_get_request_all_procedures_auth_expired_403(header_auth_expired, mock_body_re, test_client):
    """
        GIVEN the headers from the request and
        WHEN authentication is verified, but the token of authorization to expired
        THEN return a response with status 403 that the token to expired
    """
    responsec = test_client.get("/schoolServices-ces/api/requestAllProcedures/v1", headers=header_auth_expired)

    assert responsec.status_code == 403

"""
def test_get_requestAllProcedures_notfound_data_404(headers_data, test_client):
    responsec = test_client.post("/schoolServices-ces/api/requestAllProcedures/v1", headers=headers_data)

    assert responsec.status_code == 404
"""


def test_get_request_all_procedures_not_id_400(headers_not_id, test_client):
    """
        GIVEN the headers from the request and
        WHEN authentication is verified, by in the headers not exist the header Service-id
        THEN  return a response with status 400
    """
    responsec = test_client.get("/schoolServices-ces/api/requestAllProcedures/v1", headers=headers_not_id)

    assert responsec.status_code == 400


def test_get_request_all_procedures_not_name_400(headers_not_name, test_client):
    """
        GIVEN the headers from the request and
        WHEN authentication is verified, by in the headers not exist the header Service-name
        THEN  return a response with status 400
    """
    responsec = test_client.get("/schoolServices-ces/api/requestAllProcedures/v1", headers=headers_not_name)

    assert responsec.status_code == 400


def test_get_request_all_procedures_not_auth_400(headers_not_auth, test_client):
    """
        GIVEN the headers from the request and
        WHEN authentication is verified, by in the headers not exist the header Authorization
        THEN  return a response with status 400
    """
    responsec = test_client.get("/schoolServices-ces/api/requestAllProcedures/v1", headers=headers_not_auth)

    assert responsec.status_code == 400


def test_get_request_all_procedures_null_auth_400(headers_null_auth, test_client):
    """
        GIVEN the headers from the request and
        WHEN authentication is verified, by the el value of header Authorization is null
        THEN  return a response with status 400
    """
    responsec = test_client.get("/schoolServices-ces/api/requestAllProcedures/v1", headers=headers_null_auth)

    assert responsec.status_code == 400


def test_get_request_all_procedures_null_id_400(headers_null_id, test_client):
    """
        GIVEN the headers from the request and
        WHEN authentication is verified, by the el value of header Service-id is null
        THEN  return a response with status 400
    """
    responsec = test_client.get("/schoolServices-ces/api/requestAllProcedures/v1", headers=headers_null_id)

    assert responsec.status_code == 400


def test_get_request_all_procedures_null_name_400(headers_null_name, test_client):
    """
        GIVEN the headers from the request and
        WHEN authentication is verified, by the el value of header Service-name is null
        THEN  return a response with status 400
    """
    
    responsec = test_client.get("/schoolServices-ces/api/requestAllProcedures/v1", headers=headers_null_name)

    assert responsec.status_code == 400

