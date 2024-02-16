import pytest
import requests
from app import create_app
from services.logger_service import logger


@pytest.fixture(scope='module')
def test_client():
    """
        function that creates a client a cliente for tested endpoints
    """
    app = create_app()

    with app.test_client() as test_client:
        return test_client


@pytest.fixture
def mock_data_user_utc():
    """
        function to return a user of school UTC
    """
    return {
        "name": "PRUEBA CUATRO UTC VEINTE NUEVE VEINTE",
        "email": "ricardo.cervantes@edu.utc.mx",
        "studentId": 346901,
        "studentEnrollmentNumber": "220055315",
        "curp": "HEAE911221HDFRND06",
        "academicLevel": "BACHILLERATO",
        "academicLevelCode": "BA",
        "program": "TURISMO",
        "campus": "PLANTEL COACALCO",
        "phoneNumber": "5252525252",
        "periodCode": "202247",
        "cuatrimestre": "Sin Cuatrimestre Asignado",
        "modality": "A Distancia",
        "privacyNotice": {
            "privacy_notice_agreed": True,
            "terms_and_conditions_agreed": True,
            "promotions_and_discounts": True
        },
        "webApp": {
            "url": "https://app-campusvirtual-dev.azurewebsites.net",
            "school": "UTC"
        },
        "permissions": {
            "serviciosEscolares": {
                "access": True,
                "functions": {
                    "HIA": {
                        "access": True,
                        "buttons": {}
                    },
                    "CEE": {
                        "access": True,
                        "buttons": {}
                    },
                    "credencial": {
                        "access": True,
                        "buttons": {}
                    },
                    "REI": {
                        "access": False,
                        "buttons": {}
                    },
                    "COE": {
                        "access": True,
                        "buttons": {}
                    },
                    "EQU": {
                        "access": True,
                        "buttons": {}
                    },
                    "servicioSocial": {
                        "access": True,
                        "buttons": {
                            "servicioSocialGral": {
                                "access": True,
                                "validations": {
                                    "validations": {
                                        "percent": True,
                                        "documents": True
                                    }
                                }
                            }
                        }
                    },
                    "titulacion": {
                        "access": False,
                        "buttons": {
                            "cursando": {
                                "access": False,
                                "validations": {
                                    "validations": {
                                        "percent": False,
                                        "documents": False
                                    }
                                }
                            },
                            "egresado": {
                                "access": False,
                                "validations": {
                                    "validations": {
                                        "percent": False,
                                        "documents": False
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "aula": {
                "access": True,
                "functions": {}
            },
            "biblioteca": {
                "access": True,
                "functions": {}
            },
            "ayuda": {
                "access": True,
                "functions": {
                    "cap": {
                        "access": True,
                        "buttons": {}
                    },
                    "tramites": {
                        "access": True,
                        "buttons": {}
                    },
                    "tecnica": {
                        "access": True,
                        "buttons": {}
                    },
                    "preguntas": {
                        "access": True,
                        "buttons": {}
                    },
                    "financiera": {
                        "access": True,
                        "buttons": {}
                    },
                    "academica": {
                        "access": True,
                        "buttons": {}
                    }
                }
            },
            "facturas": {
                "access": False,
                "functions": {}
            },
            "estadoCuenta": {
                "access": False,
                "functions": {}
            },
            "pagos": {
                "access": True,
                "functions": {
                    "mercadoPago": {
                        "access": True,
                        "buttons": {}
                    },
                    "referencia": {
                        "access": True,
                        "buttons": {}
                    }
                }
            }
        }
    }


@pytest.fixture
def mock_data_user_ula_online():
    """
        function to return a user of school ULA
    """
    return {
        "name": "ALUMNO OL PRUEBA TREINTA Y OCHO",
        "email": "a.pruebatreintayocho@my.ula.edu.mx",
        "studentId": 127668,
        "studentEnrollmentNumber": "U99344254",
        "curp": "XXXX010101HXXXXX01",
        "academicLevel": "LICENCIATURA ONLINE 5x1",
        "academicLevelCode": "2L",
        "program": "PSICOLOGIA",
        "campus": "ONLINE",
        "phoneNumber": "5530052171",
        "periodCode": "202290",
        "cuatrimestre": "Sin Cuatrimestre Asignado",
        "modality": "A Distancia",
        "privacyNotice": {
            "privacy_notice_agreed": True,
            "terms_and_conditions_agreed": True,
            "promotions_and_discounts": False
        },
        "webApp": {
            "url": "https://espacio.ula.edu.mx",
            "school": "ULA"
        },
        "permissions": {
            "serviciosEscolares": {
                "access": True,
                "functions": {
                    "HIA": {
                        "access": True,
                        "buttons": {}
                    },
                    "CEE": {
                        "access": True,
                        "buttons": {}
                    },
                    "credencial": {
                        "access": True,
                        "buttons": {}
                    },
                    "REI": {
                        "access": False,
                        "buttons": {}
                    },
                    "COE": {
                        "access": True,
                        "buttons": {}
                    },
                    "EQU": {
                        "access": True,
                        "buttons": {}
                    },
                    "servicioSocial": {
                        "access": False,
                        "buttons": {
                            "servicioSocialGral": {
                                "access": False,
                                "validations": {
                                    "validations": {
                                        "percent": False,
                                        "documents": True
                                    }
                                }
                            }
                        }
                    },
                    "titulacion": {
                        "access": False,
                        "buttons": {
                            "cursando": {
                                "access": False,
                                "validations": {
                                    "validations": {
                                        "percent": False,
                                        "documents": False
                                    }
                                }
                            },
                            "egresado": {
                                "access": False,
                                "validations": {
                                    "validations": {
                                        "percent": False,
                                        "documents": False
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "aula": {
                "access": True,
                "functions": {}
            },
            "biblioteca": {
                "access": True,
                "functions": {}
            },
            "ayuda": {
                "access": True,
                "functions": {
                    "cap": {
                        "access": True,
                        "buttons": {}
                    },
                    "tramites": {
                        "access": True,
                        "buttons": {}
                    },
                    "tecnica": {
                        "access": True,
                        "buttons": {}
                    },
                    "preguntas": {
                        "access": True,
                        "buttons": {}
                    },
                    "financiera": {
                        "access": True,
                        "buttons": {}
                    },
                    "academica": {
                        "access": True,
                        "buttons": {}
                    }
                }
            },
            "facturas": {
                "access": False,
                "functions": {}
            },
            "estadoCuenta": {
                "access": False,
                "functions": {}
            },
            "pagos": {
                "access": True,
                "functions": {
                    "mercadoPago": {
                        "access": True,
                        "buttons": {}
                    },
                    "referencia": {
                        "access": True,
                        "buttons": {}
                    }
                }
            }
        }
    }


@pytest.fixture
def mock_data_user_ula_schooled():
    """
        function to return a user of school ULA
    """
    return {
        "name": "ALUMNO OL PRUEBA TREINTA Y OCHO",
        "email": "a.pruebatreintayocho@my.ula.edu.mx",
        "studentId": 127668,
        "studentEnrollmentNumber": "U99344254",
        "curp": "XXXX010101HXXXXX01",
        "academicLevel": "LICENCIATURA ONLINE 5x1",
        "academicLevelCode": "2L",
        "program": "PSICOLOGIA",
        "campus": "ONLINE",
        "phoneNumber": "5530052171",
        "periodCode": "202290",
        "cuatrimestre": "Sin Cuatrimestre Asignado",
        "modality": "Escolarizada",
        "privacyNotice": {
            "privacy_notice_agreed": True,
            "terms_and_conditions_agreed": True,
            "promotions_and_discounts": False
        },
        "webApp": {
            "url": "https://espacio.ula.edu.mx",
            "school": "ULA"
        },
        "permissions": {
            "serviciosEscolares": {
                "access": True,
                "functions": {
                    "HIA": {
                        "access": True,
                        "buttons": {}
                    },
                    "CEE": {
                        "access": True,
                        "buttons": {}
                    },
                    "credencial": {
                        "access": True,
                        "buttons": {}
                    },
                    "REI": {
                        "access": False,
                        "buttons": {}
                    },
                    "COE": {
                        "access": True,
                        "buttons": {}
                    },
                    "EQU": {
                        "access": True,
                        "buttons": {}
                    },
                    "servicioSocial": {
                        "access": False,
                        "buttons": {
                            "servicioSocialGral": {
                                "access": False,
                                "validations": {
                                    "validations": {
                                        "percent": False,
                                        "documents": True
                                    }
                                }
                            }
                        }
                    },
                    "titulacion": {
                        "access": False,
                        "buttons": {
                            "cursando": {
                                "access": False,
                                "validations": {
                                    "validations": {
                                        "percent": False,
                                        "documents": False
                                    }
                                }
                            },
                            "egresado": {
                                "access": False,
                                "validations": {
                                    "validations": {
                                        "percent": False,
                                        "documents": False
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "aula": {
                "access": True,
                "functions": {}
            },
            "biblioteca": {
                "access": True,
                "functions": {}
            },
            "ayuda": {
                "access": True,
                "functions": {
                    "cap": {
                        "access": True,
                        "buttons": {}
                    },
                    "tramites": {
                        "access": True,
                        "buttons": {}
                    },
                    "tecnica": {
                        "access": True,
                        "buttons": {}
                    },
                    "preguntas": {
                        "access": True,
                        "buttons": {}
                    },
                    "financiera": {
                        "access": True,
                        "buttons": {}
                    },
                    "academica": {
                        "access": True,
                        "buttons": {}
                    }
                }
            },
            "facturas": {
                "access": False,
                "functions": {}
            },
            "estadoCuenta": {
                "access": False,
                "functions": {}
            },
            "pagos": {
                "access": True,
                "functions": {
                    "mercadoPago": {
                        "access": True,
                        "buttons": {}
                    },
                    "referencia": {
                        "access": True,
                        "buttons": {}
                    }
                }
            }
        }
    }

@pytest.fixture
def mock_data_user_utc_online():
    """
        function to return a user of school ULA
    """
    return {
      "name": "PRUEBA CUATRO UTC VEINTE NUEVE VEINTE",
      "email": "ricardo.cervantes@edu.utc.mx",
      "studentId": 346901,
      "studentEnrollmentNumber": "220055315",
      "curp": "HEAE911221HDFRND06",
      "academicLevel": "BACHILLERATO",
      "academicLevelCode": "BA",
      "program": "TURISMO",
      "campus": "PLANTEL COACALCO",
      "phoneNumber": "5252525252",
      "periodCode": "202247",
      "cuatrimestre": "Sin Cuatrimestre Asignado",
      "modality": "A Distancia",
      "privacyNotice": {
        "privacy_notice_agreed": True,
        "terms_and_conditions_agreed": True,
        "promotions_and_discounts": True
      },
      "webApp": {
        "url": "https://app-campusvirtual-dev.azurewebsites.net",
        "school": "UTC"
      },
      "permissions": {
        "serviciosEscolares": {
          "access": True,
          "functions": {
            "HIA": {
              "access": True,
              "buttons": {}
            },
            "CEE": {
              "access": True,
              "buttons": {}
            },
            "credencial": {
              "access": True,
              "buttons": {}
            },
            "REI": {
              "access": False,
              "buttons": {}
            },
            "COE": {
              "access": True,
              "buttons": {}
            },
            "EQU": {
              "access": True,
              "buttons": {}
            },
            "servicioSocial": {
              "access": True,
              "buttons": {
                "servicioSocialGral": {
                  "access": True,
                  "validations": {
                    "validations": {
                      "percent": True,
                      "documents": True
                    }
                  }
                }
              }
            },
            "titulacion": {
              "access": False,
              "buttons": {
                "cursando": {
                  "access": False,
                  "validations": {
                    "validations": {
                      "percent": False,
                      "documents": False
                    }
                  }
                },
                "egresado": {
                  "access": False,
                  "validations": {
                    "validations": {
                      "percent": False,
                      "documents": False
                    }
                  }
                }
              }
            }
          }
        },
        "aula": {
          "access": True,
          "functions": {}
        },
        "biblioteca": {
          "access": True,
          "functions": {}
        },
        "ayuda": {
          "access": True,
          "functions": {
            "cap": {
              "access": True,
              "buttons": {}
            },
            "tramites": {
              "access": True,
              "buttons": {}
            },
            "tecnica": {
              "access": True,
              "buttons": {}
            },
            "preguntas": {
              "access": True,
              "buttons": {}
            },
            "financiera": {
              "access": True,
              "buttons": {}
            },
            "academica": {
              "access": True,
              "buttons": {}
            }
          }
        },
        "facturas": {
          "access": False,
          "functions": {}
        },
        "estadoCuenta": {
          "access": False,
          "functions": {}
        },
        "pagos": {
          "access": True,
          "functions": {
            "mercadoPago": {
              "access": True,
              "buttons": {}
            },
            "referencia": {
              "access": True,
              "buttons": {}
            }
          }
        }
      }
    }

@pytest.fixture
def mock_data():
    return {
        "name": "RICARDO CERVANTES LOPEZ",
        "email": "ricardo.cervantes@edu.utc.mx",
        "studentId": 346901,
        "studentEnrollmentNumber": "220055315",
        "curp": "HEAE911221HDFRND06",
        "academicLevel": "BACHILLERATO",
        "academicLevelCode": "BA",
        "program": "BACH TECNOLÓGICO EN TURISMO",
        "campus": "PLANTEL COACALCO",
        "phoneNumber": "5554279078",
        "modality": "A Distancia",
        "privacyNotice": {
            "privacy_notice_agreed": True,
            "terms_and_conditions_agreed": True,
            "promotions_and_discounts": False
        },
        "webApp": {
            "url": "https://app-campusvirtual-dev.azurewebsites.net",
            "school": "UTC"
        },
        "permissions": {
            "SES": True,
            "ATT": True,
            "PRF": True,
            "CLS": True,
            "AYC": True,
            "PRO": True,
            "INT": True,
            "DOA": True,
            "COE": True,
            "BIB": True,
            "IDU": True,
            "BEC": True,
            "HIA": True,
            "CEE": True,
            "LOG": True,
            "CAE": True,
            "EQU": True,
            "ATA": True,
            "TUT": True,
            "REE": True,
            "CAP": True,
            "PAF": True,
            "CRE": True,
            "REI": True,
            "CLA": True,
            "TIT": True
        }

    }


@pytest.fixture
def header_auth_ok_prod():
    """
        This function return a token validate for test
    """
    url = "https://app-cv-oauth-prod.azurewebsites.net/createTokens"
    response = requests.post(url).json()

    body = {"refreshToken": response['refreshToken']}

    url2 = "https://app-cv-oauth-prod.azurewebsites.net/refreshToken"

    response2 = requests.post(url2, json=body).json()

    return response2['accessToken']


@pytest.fixture
def header_auth_ok_qa():
    """
        This function return a token validate for test
    """
    url = "https://app-cv-oauth-qa.azurewebsites.net/createTokens"
    response = requests.post(url).json()

    body = {"refreshToken": response['refreshToken']}

    url2 = "https://app-cv-oauth-qa.azurewebsites.net/refreshToken"

    response2 = requests.post(url2, json=body).json()

    return response2['accessToken']


@pytest.fixture
def header_auth_ok():
    """
        This function return a token validate for test
    """
    url = "https://app-cv-oauth-dev.azurewebsites.net/createTokens"
    response = requests.post(url).json()

    body = {"refreshToken": response['refreshToken']}

    url2 = "https://app-cv-oauth-dev.azurewebsites.net/refreshToken"

    response2 = requests.post(url2, json=body).json()

    return response2['accessToken']


@pytest.fixture
def header_auth_ok_with_data(mock_data):
    """
        function that creates a token with data specific
    """
    url = "https://app-cv-oauth-dev.azurewebsites.net/createTokens"
    response = requests.post(url, json=mock_data).json()

    body = {"refreshToken": response['refreshToken']}

    url2 = "https://app-cv-oauth-dev.azurewebsites.net/refreshToken"

    response2 = requests.post(url2, json=body).json()

    return response2['accessToken']


@pytest.fixture
def header_auth_ok_with_data_utc(mock_data_user_utc_online):
    """
        function that creates a token with data specific
    """
    url = "https://app-cv-oauth-dev.azurewebsites.net/createTokens"
    response = requests.post(url, json=mock_data_user_utc_online).json()
    '''
    body = {"refreshToken": response['refreshToken']}

    url2 = "https://app-cv-oauth-dev.azurewebsites.net/refreshToken"
    
    response2 = requests.post(url2, json=body).json()
    '''

    return response['accessToken']


@pytest.fixture
def header_auth_ok_with_data_online_ula(mock_data_user_ula_online):
    """
        function that creates a token with data specific
    """
    url = "https://app-cv-oauth-dev.azurewebsites.net/createTokens"
    response = requests.post(url, json=mock_data_user_ula_online).json()

    '''
    body = {"refreshToken": response['refreshToken']}

    url2 = "https://app-cv-oauth-dev.azurewebsites.net/refreshToken"

    response2 = requests.post(url2, json=body).json()
    '''
    return response['accessToken']


@pytest.fixture
def header_auth_ok_with_data_schooled_ula(mock_data_user_ula_schooled):
    """
        function that creates a token with data specific
    """
    url = "https://app-cv-oauth-dev.azurewebsites.net/createTokens"
    response = requests.post(url, json=mock_data_user_ula_schooled).json()

    '''
    body = {"refreshToken": response['refreshToken']}

    url2 = "https://app-cv-oauth-dev.azurewebsites.net/refreshToken"

    response2 = requests.post(url2, json=body).json()
    '''
    logger.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    logger.debug(f"{response['accessToken']}")
    logger.debug(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    return response['accessToken']


@pytest.fixture
def headers(header_auth_ok):
    """
        This function return the headers necessary in the request
    """
    headers = {
        "Authorization": header_auth_ok,
        "Service-id": "virtual-campus-ss-ces-api",
        "Service-name": "SS-CES Service API"
    }
    return headers


@pytest.fixture
def headers_with_data_online_utc(header_auth_ok_with_data_utc):
    """
        This function return the headers necessary in the request
    """
    headers = {
        "Authorization": header_auth_ok_with_data_utc,
        "Service-id": "virtual-campus-ss-ces-api",
        "Service-name": "SS-CES Service API"
    }
    return headers


@pytest.fixture
def headers_with_data_online_ula(header_auth_ok_with_data_online_ula):
    """
        This function return the headers necessary in the request
    """
    headers = {
        "Authorization": header_auth_ok_with_data_online_ula,
        "Service-id": "virtual-campus-ss-ces-api",
        "Service-name": "SS-CES Service API"
    }
    return headers


@pytest.fixture
def headers_with_data_schooled_ula(header_auth_ok_with_data_schooled_ula):
    """
        This function return the headers necessary in the request
    """
    headers_schooled = {
        "Authorization": header_auth_ok_with_data_schooled_ula,
        "Service-id": "virtual-campus-ss-ces-api",
        "Service-name": "SS-CES Service API"
    }
    return headers_schooled


@pytest.fixture
def headers_qa(header_auth_ok_qa):
    """
        This function return the headers for qa necessary in the request
    """
    headers = {
        "Authorization": header_auth_ok_qa,
        "Service-id": "virtual-campus-ss-ces-api",
        "Service-name": "SS-CES Service API"
    }
    return headers


@pytest.fixture
def headers_prod(header_auth_ok_prod):
    """
        This function return the headers for prod necessary in the request
    """
    headers = {
        "Authorization": header_auth_ok_prod,
        "Service-id": "virtual-campus-ss-ces-api",
        "Service-name": "SS-CES Service API"
    }
    return headers


@pytest.fixture
def headers_data(header_auth_ok_with_data):
    """
        This function return the headers necessary in the request with data specific
    """
    headers = {
        "Authorization": header_auth_ok_with_data,
        "Service-id": "virtual-campus-ss-ces-api",
        "Service-name": "SS-CES Service API"
    }
    return headers


@pytest.fixture
def headers_null_auth():
    """
        This function return the headers necessary in the request without header "Authorization" null
    """
    headers = {
        "Authorization": "",
        "Service-id": "virtual-campus-ss-ces-api",
        "Service-name": "SS-CES Service API"
    }
    return headers


@pytest.fixture
def headers_null_id(header_auth_ok):
    """
        This function return the headers necessary in the request without header "Service-id" null
    """
    headers = {
        "Authorization": header_auth_ok,
        "Service-id": "",
        "Service-name": "SS-CES Service API"
    }
    return headers


@pytest.fixture
def headers_null_name(header_auth_ok):
    """
        This function return the headers necessary in the request without header "Service-name" null
    """
    headers = {
        "Authorization": header_auth_ok,
        "Service-id": "virtual-campus-ss-ces-api",
        "Service-name": ""
    }
    return headers


@pytest.fixture
def header_auth_invalid():
    """
        This function return the headers necessary in the request with header "Authorization" invalided
    """
    headers = {
        "Authorization": "holaeyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiUklDQVJETyBDRVJWQU5URVMgTE9QRVoiLCJlbWFpbCI6InJpY2FyZG8uY2VydmFudGVzQGVkdS51dGMubXgiLCJzdHVkZW50SWQiOjM0NjkwMSwic3R1ZGVudEVucm9sbG1lbnROdW1iZXIiOiJVOTkzNDQyNTQiLCJjdXJwIjoiSEVBRTkxMTIyMUhERlJORDA2IiwiYWNhZGVtaWNMZXZlbCI6IkJBQ0hJTExFUkFUTyIsImFjYWRlbWljTGV2ZWxDb2RlIjoiQkEiLCJwcm9ncmFtIjoiQkFDSCBURUNOT0zDk0dJQ08gRU4gVFVSSVNNTyIsImNhbXB1cyI6IlBMQU5URUwgQ09BQ0FMQ08iLCJwaG9uZU51bWJlciI6IjU1NTQyNzkwNzgiLCJtb2RhbGl0eSI6IkEgRGlzdGFuY2lhIiwicHJpdmFjeU5vdGljZSI6eyJwcml2YWN5X25vdGljZV9hZ3JlZWQiOnRydWUsInRlcm1zX2FuZF9jb25kaXRpb25zX2FncmVlZCI6dHJ1ZSwicHJvbW90aW9uc19hbmRfZGlzY291bnRzIjpmYWxzZX0sIndlYkFwcCI6eyJ1cmwiOiJodHRwczovL2FwcC1jYW1wdXN2aXJ0dWFsLWRldi5henVyZXdlYnNpdGVzLm5ldCIsInNjaG9vbCI6IlVUQyJ9LCJwZXJtaXNzaW9ucyI6eyJTRVMiOnRydWUsIkFUVCI6dHJ1ZSwiUFJGIjp0cnVlLCJDTFMiOnRydWUsIkFZQyI6dHJ1ZSwiUFJPIjp0cnVlLCJJTlQiOnRydWUsIkRPQSI6dHJ1ZSwiQ09FIjp0cnVlLCJCSUIiOnRydWUsIklEVSI6dHJ1ZSwiQkVDIjp0cnVlLCJISUEiOnRydWUsIkNFRSI6dHJ1ZSwiTE9HIjp0cnVlLCJDQUUiOnRydWUsIkVRVSI6dHJ1ZSwiQVRBIjp0cnVlLCJUVVQiOnRydWUsIlJFRSI6dHJ1ZSwiQ0FQIjp0cnVlLCJQQUYiOnRydWUsIkNSRSI6dHJ1ZSwiQ0xBIjp0cnVlLCJUSVQiOnRydWV9LCJpYXQiOjE2NDE1MDU5NzgsImV4cCI6MTY0MTUwNjg3OH0.hLLL0Xy-U9zn1gr3Plg2WfixLkTuJl-mKzcCE6ZkcJU",
        "Service-id": "virtual-campus-ss-ces-api",
        "Service-name": "SS-CES Service API"
    }
    return headers


@pytest.fixture
def header_auth_expired():
    """
        This function return the headers necessary in the request with header "Authorization" expired
    """
    headers = {
        "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiUklDQVJETyBDRVJWQU5URVMgTE9QRVoiLCJlbWFpbCI6InJpY2FyZG8uY2VydmFudGVzQGVkdS51dGMubXgiLCJzdHVkZW50SWQiOjM0NjkwMSwic3R1ZGVudEVucm9sbG1lbnROdW1iZXIiOiJVOTkzNDQyNTQiLCJjdXJwIjoiSEVBRTkxMTIyMUhERlJORDA2IiwiYWNhZGVtaWNMZXZlbCI6IkJBQ0hJTExFUkFUTyIsImFjYWRlbWljTGV2ZWxDb2RlIjoiQkEiLCJwcm9ncmFtIjoiQkFDSCBURUNOT0zDk0dJQ08gRU4gVFVSSVNNTyIsImNhbXB1cyI6IlBMQU5URUwgQ09BQ0FMQ08iLCJwaG9uZU51bWJlciI6IjU1NTQyNzkwNzgiLCJtb2RhbGl0eSI6IkEgRGlzdGFuY2lhIiwicHJpdmFjeU5vdGljZSI6eyJwcml2YWN5X25vdGljZV9hZ3JlZWQiOnRydWUsInRlcm1zX2FuZF9jb25kaXRpb25zX2FncmVlZCI6dHJ1ZSwicHJvbW90aW9uc19hbmRfZGlzY291bnRzIjpmYWxzZX0sIndlYkFwcCI6eyJ1cmwiOiJodHRwczovL2FwcC1jYW1wdXN2aXJ0dWFsLWRldi5henVyZXdlYnNpdGVzLm5ldCIsInNjaG9vbCI6IlVUQyJ9LCJwZXJtaXNzaW9ucyI6eyJTRVMiOnRydWUsIkFUVCI6dHJ1ZSwiUFJGIjp0cnVlLCJDTFMiOnRydWUsIkFZQyI6dHJ1ZSwiUFJPIjp0cnVlLCJJTlQiOnRydWUsIkRPQSI6dHJ1ZSwiQ09FIjp0cnVlLCJCSUIiOnRydWUsIklEVSI6dHJ1ZSwiQkVDIjp0cnVlLCJISUEiOnRydWUsIkNFRSI6dHJ1ZSwiTE9HIjp0cnVlLCJDQUUiOnRydWUsIkVRVSI6dHJ1ZSwiQVRBIjp0cnVlLCJUVVQiOnRydWUsIlJFRSI6dHJ1ZSwiQ0FQIjp0cnVlLCJQQUYiOnRydWUsIkNSRSI6dHJ1ZSwiQ0xBIjp0cnVlLCJUSVQiOnRydWV9LCJpYXQiOjE2NDE1MDc1MjYsImV4cCI6MTY0MTUwODQyNn0.Lxf-6__O_KdviufijPInNWQz4OqlXlqe-CKrQeV9x1I",
        "Service-id": "virtual-campus-ss-ces-api",
        "Service-name": "SS-CES Service API"
    }
    return headers


@pytest.fixture
def headers_not_auth():
    """
        This function return the headers necessary in the request without header "Authorization"
    """
    headers = {
        "Service-id": "virtual-campus-ss-ces-api",
        "Service-name": "SS-CES Service API"
    }
    return headers


@pytest.fixture
def headers_not_id(header_auth_ok):
    """
        This function return the headers necessary in the request without header "Service-id"
    """
    headers = {
        "Authorization": header_auth_ok,
        "Service-name": "SS-CES Service API"
    }
    return headers


@pytest.fixture
def headers_not_name(header_auth_ok):
    """
        This function return the headers necessary in the request without header "Service-name"
    """
    headers = {
        "Authorization": header_auth_ok,
        "Service-id": "virtual-campus-ss-ces-api",
    }
    return headers


@pytest.fixture
def mock_body_re():
    """
        This function return a request body with data necessary to request
    """
    return {
        "chargeAccepted": True,
        "comments": "string",
        "files": [
            {
                "fileBody": "string",
                "fileName": "string",
                "fileType": "string"
            }
        ],
        "phoneNumber": "string"
    }


@pytest.fixture
def mock_body_re2():
    """
        This function return a request body with data necessary to request
    """
    return {
        "phoneNumber": "1234567890",
        "chargeAccepted": True,
        "recordTypeId": "0127h000000g8TTAAY",
        "paymentTypeValue": "GRA12M13",
        "programTypeValue": "PSI102018O",

        "typeValue": None,
        "description": "test",
        "files": [
            {
                "fileBody": "string",
                "fileName": "string",
                "fileType": "string"
            }
        ],

    }


@pytest.fixture
def mock_body_re_reinstatement_ula():
    """
        This function return a request body with data necessary for endpoint 'POST' reinstatement ULA
    """
    return {
        "phoneNumber": "1234567890",
        "chargeAccepted": True,
        "comments": "test comments",
        "files": [
            {
                "fileName": "test.pdf",
                "fileBody": "aG9sYSBtdW5kbyBkZXNkZSBiYWNr",
                "fileType": "application/pdf"
            }
        ],
        "countryOfBirth": "Colombia",
        "countryOfPriorStudies": "Colombia",
        "schoolOfOrigin": "Colombia",
        "street": "Antillean",
        "number": "123",
        "neighborhood": "Kibana",
        "cp": "1234",
        "population": "Hura ya",
        "city": "Bente",
        "entity": "Caracas",
        "schoolPhone": "123123",
        "schoolEmail": "fere@gmail.com",
        "startDatePreviousLevel": "01/06/2000",
        "endDatePreviousLevel": "01/06/2006"

    }


@pytest.fixture(name="br_without_param_1")
def mock_body_re_reinstatement_ula_without_param_country_of_birth():
    """
        This function return a request body with data necessary for endpoint 'POST' reinstatement ULA
    """
    return {
        "phoneNumber": "1234567890",
        "chargeAccepted": True,
        "comments": "test comments",
        "files": [
            {
                "fileName": "test.pdf",
                "fileBody": "aG9sYSBtdW5kbyBkZXNkZSBiYWNr",
                "fileType": "application/pdf"
            }
        ],
        "countryOfPriorStudies": "Colombia",
        "schoolOfOrigin": "Colombia",
        "street": "Antillean",
        "number": "123",
        "neighborhood": "Kibana",
        "cp": "1234",
        "population": "Hura ya",
        "city": "Bente",
        "entity": "Caracas",
        "schoolPhone": "123123",
        "schoolEmail": "fere@gmail.com",
        "startDatePreviousLevel": "01/06/2000",
        "endDatePreviousLevel": "01/06/2006"

    }


@pytest.fixture(name="br_without_param_2")
def mock_body_re_reinstatement_ula_without_param_country_of_prior_studies():
    """
        This function return a request body with data necessary for endpoint 'POST' reinstatement ULA
    """
    return {
        "phoneNumber": "1234567890",
        "chargeAccepted": True,
        "comments": "test comments",
        "files": [
            {
                "fileName": "test.pdf",
                "fileBody": "aG9sYSBtdW5kbyBkZXNkZSBiYWNr",
                "fileType": "application/pdf"
            }
        ],
        "countryOfBirth": "Colombia",
        "schoolOfOrigin": "Colombia",
        "street": "Antillean",
        "number": "123",
        "neighborhood": "Kibana",
        "cp": "1234",
        "population": "Hura ya",
        "city": "Bente",
        "entity": "Caracas",
        "schoolPhone": "123123",
        "schoolEmail": "fere@gmail.com",
        "startDatePreviousLevel": "01/06/2000",
        "endDatePreviousLevel": "01/06/2006"
    }


@pytest.fixture
def mock_body_re_reinstatement_utc():
    """
        This function return a request body with data necessary for endpoint 'POST' reinstatement UTC
    """
    return {
        "chargeAccepted": True,
        "comments": "test comments",
        "files": [
            {
                "fileName": "test.pdf",
                "fileBody": "aG9sYSBtdW5kbyBkZXNkZSBiYWNr",
                "fileType": "application/pdf"
            }
        ],
        "phoneNumber": "1234567890"
    }


@pytest.fixture
def mock_body_re_degree_online_ula():
    """
        This function return a request body with data necessary for endpoint 'POST' degree online ULA
    """
    return {
        "phoneNumber": "1234567890",
        "chargeAccepted": True,
        "recordTypeId": "0127h000000g8TTAAY",
        "paymentTypeValue": "GRA12M13",
        "programTypeValue": "PSI102018O",

        "typeValue": None,
        "description": "test",

        "files": [
            {
                "fileName": "Solicitud_en_trámite_Titulación.pdf",
                "fileBody": "aG9sYSBtdW5kbyBkZXNkZSBiYWNr",
                "fileType": "application/pdf"
            },
            {
                "fileName": "Fotografía_tamaña_ovalo.pdf",
                "fileBody": "aG9sYSBtdW5kbyBkZXNkZSBiYWNr",
                "fileType": "application/pdf"
            },
            {
                "fileName": "Historia_académica.pdf",
                "fileBody": "aG9sYSBtdW5kbyBkZXNkZSBiYWNr",
                "fileType": "application/pdf"
            },
            {
                "fileName": "Identificación_oficial_reciente.pdf",
                "fileBody": "aG9sYSBtdW5kbyBkZXNkZSBiYWNr",
                "fileType": "application/pdf"
            },
            {
                "fileName": "CURP.pdf",
                "fileBody": "aG9sYSBtdW5kbyBkZXNkZSBiYWNr",
                "fileType": "application/pdf"
            },
            {
                "fileName": "Liberación_de_servicio_social_ULA.pdf",
                "fileBody": "aG9sYSBtdW5kbyBkZXNkZSBiYWNr",
                "fileType": "application/pdf"
            }
        ]
    }


@pytest.fixture
def mock_body_re_degree_schooled_ula():
    """
      This function return a request body with data necessary for endpoint 'POST' degree online ULA
    """
    return {
        "phoneNumber": "1234567890",
        "chargeAccepted": True,
        "recordTypeId": "0124X000001NffeQAC",
        "paymentTypeValue": None,
        "description": "test",
        "typeValue": "TRAS9",

        "files": [
            {
                "fileName": "Solicitud_en_trámite_Titulación.pdf",
                "fileBody": "aG9sYSBtdW5kbyBkZXNkZSBiYWNr",
                "fileType": "application/pdf"
            },
            {
                "fileName": "Fotografía_tamaña_ovalo.pdf",
                "fileBody": "aG9sYSBtdW5kbyBkZXNkZSBiYWNr",
                "fileType": "application/pdf"
            },
            {
                "fileName": "Historia_académica.pdf",
                "fileBody": "aG9sYSBtdW5kbyBkZXNkZSBiYWNr",
                "fileType": "application/pdf"
            },
            {
                "fileName": "Identificación_oficial_reciente.pdf",
                "fileBody": "aG9sYSBtdW5kbyBkZXNkZSBiYWNr",
                "fileType": "application/pdf"
            },
            {
                "fileName": "CURP.pdf",
                "fileBody": "aG9sYSBtdW5kbyBkZXNkZSBiYWNr",
                "fileType": "application/pdf"
            },
            {
                "fileName": "Liberación_de_servicio_social_ULA.pdf",
                "fileBody": "aG9sYSBtdW5kbyBkZXNkZSBiYWNr",
                "fileType": "application/pdf"
            }
        ]
    }


@pytest.fixture
def mock_body_re_equivalence_utc():
    """
        This function return a request body with data necessary for endpoint 'POST' equivalence UTC
    """
    return {
        "chargeAccepted": True,
        "comments": "string",
        "files": [
            {
                "fileBody": "string",
                "fileName": "string",
                "fileType": "string"
            }
        ],
        "phoneNumber": "string"
    }
