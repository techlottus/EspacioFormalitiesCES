# python modules
from werkzeug.wrappers import Request, Response
import json
import requests
# constants
from constants.identifiers_constants import Service_Id, Authorization
from constants.messages import unavailable_service_info, bad_service_id, no_service_id, bad_service_name, \
    no_auth_header, no_service_name
from constants.ssces_constants import *
from constants.routes import SERVICE_URLS
from constants.services_urls import OAUTH_URL
# services
from services.logger_service import logger
from services.set_responses_service import error_response_auth


def set_bad_request_response(error_message):
    """
    sets Bad Request response in Authorization Class
    """
    bad_request_error['error']['message'] = error_message
    bad_req_error_response = Response(json.dumps(bad_request_error), mimetype='application/json', status=400)
    return bad_req_error_response


def set_auth_error_response(status_code, message):
    """
    sets Authentication Error response in Authorization Class
    """
    if status_code == 503:
        status_info = unavailable_service_info
    else:
        status_info = None
    auth_error_response = Response(json.dumps(error_response_auth(status_code, message, status_info)),
                                   mimetype='application/json', status=status_code)
    return auth_error_response


def validate_headers():
    pass


class AuthorizationMiddleware:
    """
    Authorization Middleware
    """
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        logger.debug(f'{AuthorizationMiddleware.__name__} accessed.')
        request = Request(environ)
        # just validate headers when URL is one of the service routes
        for route in SERVICE_URLS:
            if route in request.url:
                logger.info(f"URL accessed: {request.url}")
                headers = request.headers
                logger.debug(f"headers: {headers}")
                if Service_Id in headers:
                    if SERVICE_ID != headers[Service_Id]:
                        logger.error(f"bad Service-Id: {headers[Service_Id]}")
                        return set_bad_request_response(bad_service_id)(environ, start_response)
                else:
                    logger.error("No Service-Id")
                    return set_bad_request_response(no_service_id)(environ, start_response)
                service_name = 'Service-Name'
                if service_name in headers:
                    if SERVICE_NAME != headers[service_name]:
                        logger.error(f"Bad Service-Name: {headers[service_name]}")
                        return set_bad_request_response(bad_service_name)(environ, start_response)
                else:
                    logger.error("No Service-Name")
                    return set_bad_request_response(no_service_name)(environ, start_response)
                # Validate access token
                if Authorization not in headers:
                    logger.error("No access token provided")
                    return set_bad_request_response(no_auth_header)(environ, start_response)
                else:
                    auth_header = headers[Authorization]
                    oauth_headers = {Authorization: auth_header}
                    try:
                        # try to reach communication with Oauth
                        logger.debug(f"Validating access token with oauth service at: {OAUTH_URL}")
                        oauth_response = requests.get(OAUTH_URL, headers=oauth_headers)
                        json_response = oauth_response.json()
                        status_code = oauth_response.status_code
                        logger.debug(f"oauth response: {json_response}: {status_code}")
                    except Exception as e:
                        # communication with Oauth failed
                        logger.error(e)
                        logger.error("Communication with Oauth failed.")
                        return set_auth_error_response(503, "Communication with Oauth failed")(environ, start_response)
                    else:
                        if status_code != 200:
                            oauth_err_message = json_response['message']
                            return set_auth_error_response(status_code, oauth_err_message)(environ, start_response)
                # if this line is reached, then access is granted
                logger.debug("Headers validated successfully")
                return self.app(environ, start_response)
                # return 'hola'
        logger.debug(f"Skipping validation from URL: {request.url}")
        return self.app(environ, start_response)
