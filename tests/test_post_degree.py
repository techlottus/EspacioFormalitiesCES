from app import create_app
from services.authorization_service import Authorization
from tests.commons import *


def test_post_degree_ula_online_201(headers_with_data_online_ula,
                                    mock_body_re_degree_online_ula,
                                    test_client):
    """
        GIVEN the headers and body request from the request and
        WHEN authentication is verified
        THEN to create new resource with the data of body request
    """
    response = test_client.post("/schoolServices-ces/api/degree/v1",
                                headers=headers_with_data_online_ula,
                                json=mock_body_re_degree_online_ula)

    assert response.status_code == 201


#@pytest.mark.smoke
def test_post_degree_ula_schooled_201(headers_with_data_schooled_ula,
                                      mock_body_re_degree_schooled_ula,
                                      test_client):
    """
        GIVEN the headers and body request from the request and
        WHEN authentication is verified
        THEN to create new resource with the data of body request
    """
    response = test_client.post("/schoolServices-ces/api/degree/v1",
                                headers=headers_with_data_schooled_ula,
                                json=mock_body_re_degree_schooled_ula)

    assert response.status_code == 201


def test_post_degree_ula_auth_invalid_401(header_auth_invalid, mock_body_re_degree_online_ula, test_client):
    """
        GIVEN the headers from the request and
        WHEN authentication is verified, but the authorization is not a correct token
        THEN return a response with status 401 that the token is invalid
    """
    response = test_client.post("/schoolServices-ces/api/degree/v1",
                                headers=header_auth_invalid, json=mock_body_re_degree_online_ula)

    assert response.status_code == 401


def test_post_degree_ula_auth_expired_403(header_auth_expired, mock_body_re_degree_online_ula, test_client):
    """
        GIVEN the headers from the request and
        WHEN authentication is verified, but the token of authorization to expired
        THEN return a response with status 403 that the token to expired
    """
    response = test_client.post("/schoolServices-ces/api/degree/v1",
                                headers=header_auth_expired, json=mock_body_re_degree_online_ula)

    assert response.status_code == 403


def test_post_degree_ula_not_id_400(headers_not_id, mock_body_re_degree_online_ula, test_client):
    """
        GIVEN the headers from the request and
        WHEN authentication is verified, by in the headers not exist the header Service-id
        THEN  return a response with status 400
    """
    responsec = test_client.get("/schoolServices-ces/api/degree/v1",
                                headers=headers_not_id, json=mock_body_re_degree_online_ula)

    assert responsec.status_code == 400


def test_post_degree_ula_not_name_400(headers_not_name, mock_body_re_degree_online_ula, test_client):
    """
        GIVEN the headers from the request and
        WHEN authentication is verified, by in the headers not exist the header Service-name
        THEN  return a response with status 400
    """
    response = test_client.get("/schoolServices-ces/api/degree/v1",
                               headers=headers_not_name, json=mock_body_re_degree_online_ula)

    assert response.status_code == 400


def test_post_degree_ula_not_auth_400(headers_not_auth, mock_body_re_degree_online_ula, test_client):
    """
        GIVEN the headers from the request and
        WHEN authentication is verified, by in the headers not exist the header Authorization
        THEN  return a response with status 400
    """
    response = test_client.get("/schoolServices-ces/api/degree/v1",
                               headers=headers_not_auth, json=mock_body_re_degree_online_ula)

    assert response.status_code == 400


def test_post_degree_ula_null_id_400(headers_null_id, mock_body_re_degree_online_ula, test_client):
    """
        GIVEN the headers from the request and
        WHEN authentication is verified, by the el value of header Service-id is null
        THEN  return a response with status 400
    """
    response = test_client.get("/schoolServices-ces/api/degree/v1",
                               headers=headers_null_id, json=mock_body_re_degree_online_ula)

    assert response.status_code == 400


def test_post_degree_ula_null_name_400(headers_null_name, mock_body_re_degree_online_ula, test_client):
    """
        GIVEN the headers from the request and
        WHEN authentication is verified, by the el value of header Service-name is null
        THEN  return a response with status 400
    """
    response = test_client.get("/schoolServices-ces/api/degree/v1",
                               headers=headers_null_name, json=mock_body_re_degree_online_ula)

    assert response.status_code == 400
