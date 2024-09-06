# python modules
from flask_openapi3 import Info, HTTPBearer, OpenAPI
from werkzeug.utils import redirect
# constants
from constants.ssces_constants import *
from constants.routes import SWAGGER_URL
# services
from services.logger_service import logger
from services.authorization_service import AuthorizationMiddleware
# apps
from apps.degree_app import degree
from apps.equivalence_of_studies_app import equivalence_of_studies
from apps.reinstatement_app import reinstatement
from apps.revalidation_app import revalidation
from apps.tickets_app import tickets_api


def create_app():

    # OpenAPI config
    info = Info(title='SchoolServices - CredEquivSol, API', version='1.25.0')
    security_schemes = {"jwt": HTTPBearer(bearerFormat="JWT")}

    # set app using OpenAPI
    app = OpenAPI(__name__, info=info, securitySchemes=security_schemes)

    # setup with the configuration provided
    app.config.from_object('config.DevelopmentConfig')

    # AUTHORIZATION MIDDLEWARE
    app.wsgi_app = AuthorizationMiddleware(app.wsgi_app)

    # register apps
    app.register_api(degree)
    app.register_api(equivalence_of_studies)
    app.register_api(reinstatement)
    app.register_api(revalidation)
    app.register_api(tickets_api)

    @app.route('/')
    def redirect_to_swagger():
        return redirect(SWAGGER_URL)

    return app


if __name__ == "__main__":
    logger.info(f"{SERVICE_NAME} running at port: {PORT}")
    create_app().run(host=HOST, port=PORT)
