import pytest
from services.authorization_service import *
from utils.decoder import token_decoder

"""
@pytest.fixture
def header_auth_ok():
    url = "https://app-cv-oauth-dev.azurewebsites.net/createTokens"
    response = requests.post(url).json()

    return {
        "Authorization": "Bearer " + response['accessToken'],
    }


@pytest.fixture
def header_auth_Invalid():

    return  {
        "Authorization": "Bearer " + "ffeyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiQWxlamFuZHJvIExvcmEiLCJlbWFpbCI6InJpY2FyZG8uY2VydmFudGVzQGVkdS51dGMubXgiLCJpYXQiOjE2NDE0ODg3MTUsImV4cCI6MTY0MTQ4OTYxNX0.4Ydxkqs-6DzM7uXIUNmUmSMVtKwLzwQAj-7pBeA2w7k"
    }


@pytest.fixture
def header_auth_expired():
    return {
        "Authorization": "Bearer " + "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiQWxlamFuZHJvIExvcmEiLCJlbWFpbCI6InJpY2FyZG8uY2VydmFudGVzQGVkdS51dGMubXgiLCJpYXQiOjE2NDE0ODg3MTUsImV4cCI6MTY0MTQ4OTYxNX0.4Ydxkqs-6DzM7uXIUNmUmSMVtKwLzwQAj-7pBeA2w7k"
    }




@pytest.mark.parametrize("header, expected",[
    ('header_auth_Invalid', {"error": True, "message": "Invalid jwt", "status_code": 401}),
    #('header_auth_expired', {"error": True, "message": "Jwt has expired", "status_code": 403}),
])
def test_token_decoder_errors(header, expected):

    assert token_decoder(header) == expected
"""

"""


def test_token_decoder_ok(header_auth_ok):

    assert token_decoder(header_auth_ok)

"""