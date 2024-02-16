from tests.commons import *


def test_post_reinstatement_ula_schooled_201(headers_with_data_schooled_ula,
                                             mock_body_re_reinstatement_ula, test_client):
    """
        GIVEN the headers and body request from the request and
        WHEN authentication is verified
        THEN to create new resource with the data of body request
    """
    responsec = test_client.post("/schoolServices-ces/api/reinstatement/v1", headers=headers_with_data_schooled_ula,
                                 json=mock_body_re_reinstatement_ula)

    assert responsec.status_code == 201


def test_post_reinstatement_ula_online_201(headers_with_data_online_ula, mock_body_re_reinstatement_ula, test_client):
    """
        GIVEN the headers and body request from the request and
        WHEN authentication is verified
        THEN to create new resource with the data of body request
    """
    responsec = test_client.post("/schoolServices-ces/api/reinstatement/v1", headers=headers_with_data_online_ula,
                                 json=mock_body_re_reinstatement_ula)

    assert responsec.status_code == 201


'''
@pytest.mark.parametrize("body_request, expected, headers, test_client", [
    ("br_without_param_2", 422, headers_with_data_schooled_ula, test_client),
    ("br_without_param_1", 422, headers_with_data_schooled_ula, test_client),
])
def test_post_reinstatement_422(body_request, expected, headers, test_client):
    """
    Feature:

    Scenario:
        GIVEN the headers and body request from the request and
        WHEN authentication is verified
        THEN to create new resource with the data of body request

    Examples:

    """
    response = test_client.post("/schoolServices-ces/api/reinstatement/v1",
                                headers=headers, json=body_request)

    assert response.status_code == expected

'''


def test_post_reinstatement_without_param_1_422(headers_with_data_schooled_ula, br_without_param_1, test_client):
    """
        GIVEN the headers and body request from the request and
        WHEN authentication is verified
        THEN to create new resource with the data of body request
    """
    response = test_client.post("/schoolServices-ces/api/reinstatement/v1", headers=headers_with_data_schooled_ula,
                                json=br_without_param_1)

    assert response.status_code == 422


def test_post_reinstatement_without_param_2_422(headers_with_data_schooled_ula, br_without_param_2, test_client):
    """
        GIVEN the headers and body request from the request and
        WHEN authentication is verified
        THEN to create new resource with the data of body request
    """
    response = test_client.post("/schoolServices-ces/api/reinstatement/v1", headers=headers_with_data_schooled_ula,
                                json=br_without_param_2)

    assert response.status_code == 422


def test_post_reinstatement_auth_invalid_401(header_auth_invalid, mock_body_re, test_client):
    """
        GIVEN the headers from the request and
        WHEN authentication is verified, but the authorization is not a correct token
        THEN return a response with status 401 that the token is invalid
    """
    responsec = test_client.post("/schoolServices-ces/api/reinstatement/v1", headers=header_auth_invalid, json=mock_body_re)

    assert responsec.status_code == 401


def test_post_reinstatement_auth_expired_403(header_auth_expired, mock_body_re, test_client):
    """
        GIVEN the headers from the request and
        WHEN authentication is verified, but the token of authorization to expired
        THEN return a response with status 403 that the token to expired
    """
    responsec = test_client.post("/schoolServices-ces/api/reinstatement/v1", headers=header_auth_expired, json=mock_body_re)

    assert responsec.status_code == 403


def test_post_reinstatement_not_id_400(headers_not_id, mock_body_re, test_client):
    """
        GIVEN the headers from the request and
        WHEN authentication is verified, by in the headers not exist the header Service-id
        THEN  return a response with status 400
    """
    responsec = test_client.get("/schoolServices-ces/api/reinstatement/v1", headers=headers_not_id, json=mock_body_re)

    assert responsec.status_code == 400


def test_post_reinstatement_not_name_400(headers_not_name, mock_body_re, test_client):
    """
        GIVEN the headers from the request and
        WHEN authentication is verified, by in the headers not exist the header Service-name
        THEN  return a response with status 400
    """
    responsec = test_client.get("/schoolServices-ces/api/reinstatement/v1", headers=headers_not_name, json=mock_body_re)

    assert responsec.status_code == 400


def test_post_reinstatement_not_auth_400(headers_not_auth, mock_body_re, test_client):
    """
        GIVEN the headers from the request and
        WHEN authentication is verified, by in the headers not exist the header Authorization
        THEN  return a response with status 400
    """
    responsec = test_client.get("/schoolServices-ces/api/reinstatement/v1", headers=headers_not_auth, json=mock_body_re)

    assert responsec.status_code == 400


def test_post_reinstatement_null_id_400(headers_null_id, mock_body_re, test_client):
    """
        GIVEN the headers from the request and
        WHEN authentication is verified, by the el value of header Service-id is null
        THEN  return a response with status 400
    """
    responsec = test_client.get("/schoolServices-ces/api/reinstatement/v1", headers=headers_null_id, json=mock_body_re)

    assert responsec.status_code == 400


def test_post_reinstatement_null_name_400(headers_null_name, mock_body_re, test_client):
    """
        GIVEN the headers from the request and
        WHEN authentication is verified, by the el value of header Service-name is null
        THEN  return a response with status 400
    """
    responsec = test_client.get("/schoolServices-ces/api/reinstatement/v1", headers=headers_null_name, json=mock_body_re)

    assert responsec.status_code == 400



