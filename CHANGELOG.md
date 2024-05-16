# Changelog - SchoolServices - CredEquivSol

## [1.24.0] - 2024-05-16

Eduardo Izquierdo Rojas

### Changed:
Exceptions were added to break the flow, 
for when a detail code is not found in the detail code collection "SS_DetailCodes", 
as well as the exception for when the cost for a specific detail code does not exist,
- services/degree_service.py

The log service was modified so that it generates log files per day 
and not just one file each time the service is restarted
- services/logger_service.py


## [1.23.1] - 2023-11-10

Yair Valdivia

### Changed:
- programs_service:
  - at format_programs 

## [1.23.0] - 2023-09-04

René Alejandro Rivas

### Changed:
- tickets_service:
  - at set_tickets_list_with_medallia_flags():
    - validation to remove tickets with status 'Nuevo' and five days old removed
    - refactor setting ticket_evaluated
  - at set_trans_nums_to_tickets_list():
    - improved exception handling 

## [1.22.3] - 2023-08-14

Yair Valdivia

Change in version 
- CHANGELOG.md
- app.py

Change of flag "certificateImmigrationForm" always false
- services/programs_service.py

## [1.22.2] - 2023-08-14

Eduardo Izquierdo Rojas

Change in version 
- CHANGELOG.md
- app.py

Change in param "list_detail_codes"
- apps/degree_app.py

Change of flag "apostilledTitleForForeigners" always false
- services/programs_service.py

Brief correction in logs
- services/degree_service.py
- services/costs_service.py



## [1.22.1] - 2023-08-01

Eduardo Izquierdo Rojas

### Changed:

Brief change in version  
- CHANGELOG.md
- app.py

Addition of flags in recordtype array only for degreeInProgress (Titulación Cursando (Online)),

- services/programs_service.py
- services/degree_service.py



## [1.22.0] - 2023-07-28

Eduardo Izquierdo Rojas

### Changed:

Brief change in version  
- CHANGELOG.md
- app.py


Addition of flags in programs array, when consulting endpoint GET of degree service
and moved function "get_flags" of degree service to programs servive
- services/degree_service.py
- services/programs_service.py



## [1.21.2] - 2023-07-28

Eduardo Izquierdo Rojas

### Changed:
Brief change in version  
- CHANGELOG.md
- app.py

Addition of validation to only send the program arrangement with 100 credits
- services/programs_service.py

## [1.21.1] - 2023-07-27

Eduardo Izquierdo Rojas

### Changed:

Brief change in version  
- CHANGELOG.md
- app.py

correction of duplicate data bugs in consultation of degree programs, 
a validation was added to avoid duplicate elements
- services/programs_service.py

## [1.21.0] - 2023-07-21

Eduardo Izquierdo Rojas

### Changed:

Brief change in version  
- CHANGELOG.md
- app.py

Refactor and update of new properties in GET endpoint, level-dependent flags were added 
to determine that different documents should be displayed: "liberationOfEnglish" 
"liberationOfSocialService", "copyOfBachelorsDegree", "apostilledTitleForForeigners" 
"copyOfBachelors" , "certificateImmigrationForm" 

- apps/degree_app.py
- services/degree_service.py

Brief change of property of 'name' to 'value'
- services/programs_service.py

return to previous configuration and operation of logs (pending to finish refactor)
- services/logger_service.py


## [1.20.5] - 2023-06-22

Eduardo Izquierdo Rojas

Addition of configuration TimedRotatingFileHandler for logger service 
and create new log file each day at midnight

- services/logger_service.py

change in version 
- CHANGELOG.md 
- app.py


## [1.20.4] - 2023-06-22

Eduardo Izquierdo Rojas

Addition of flag "evaluationFlag" and identifier "ProceduresServices" to identify ticket has not been evaluated 
- services/tickets_service.py

Addition of repository to check evaluated tickets
- repositories/ADS_Scores_Medallia_repository.py

change in version 
- CHANGELOG.md
- app.py


## [1.20.3] - 2023-06-06

Eduardo Izquierdo Rojas

Refactor and rename services.
it was renamed reinstatement service to  revalidation service for ULA
it was renamed revalidation service to  reinstatement service for UTC

- apps/reinstatement_app.py
- apps/revalidation_app.py

it changed request body's for services reinstatement and revalidation
- OpenAPI/reinstatement_openapi.py
- OpenAPI/revalidation_openapi.py
- services/set_servicio_fields.py

Change in version 
- CHANGELOG.md
- app.py

## [1.20.2] - 2023-04-18

Eduardo Izquierdo Rojas

Change in version 
- CHANGELOG.md
- app.py

Correction in request body for requests in reinstatement
- OpenAPI/reinstatement_openapi.py
- OpenAPI/revalidation_openapi.py
- apps/reinstatement_app.py
- apps/revalidation_app.py
- services/set_servicio_fields.py


## [1.20.1] - 2023-03-02

Eduardo Izquierdo Rojas

### Changed:

Addition of validation and get total size files 'validate_total_files_size() not maximum to 5MB'
- `OpenAPI\commons.py`

Addition of constant 'MAX_LIMIT_SIZE'
- `constants\ssces_constants.py`

Change in version
- `app.py`
- `CHANGELOG.md`




## [1.20.0] - 2023-03-02

René Alejandro Rivas

### Added:
- `revalidation_app.py` to handle revalidation procedure 
- `revalidation_openapi.py` to handle request body validations and swagger documentation of revalidation procedure
- revalidation route added
- 
### Changed:
- at `set_servicio_fields.py`: "set_reinstatement_fields()" renamed to "set_revalidation_fields()" 
- 
### Deleted:
- ReinstatementRequestBody from reinstatement_openapi (not needed)
- 
## [1.19.1] - 2023-02-08
Eduardo Izquierdo Rojas

### Changed:
Addition of validations and Exception when searching for programs, 
when sent by the request body, and they do not exist

- services/degree_record_types_service.py

Fix when querying backed up picklist elements in mongo

- services/set_servicio_fields.py



Change in version API
- CHANGELOG.md
- app.py


## [1.19.0] - 2023-01-26

Eduardo Izquierdo Rojas

### Changed:

##### The query of existing programs to choose from was added to the controller
- apps/degree_app.py
##### conditional to obtain programs only in graduates
- services/degree_service.py
##### Addition of practical theoretical exam options
- services/set_servicio_fields.py

Change in version 
- CHANGELOG.md
- app.py


## [1.18.2] - 2023-01-17

Eduardo Izquierdo Rojas

### Changed:
Refactor and correction of validation of size in files, to make the request
and send files of no more than 2MB

- OpenAPI/commons.py

change in version 
- app.py
- CHANGELOG.md


## [1.18.1] - 2022-12-15

Eduardo Izquierdo Rojas

### Changed:
Refactor and correction of cycles when consuming service
-apps/degree_app.py
-services/costs_service.py
-services/degree_service.py

Change in version
- CHANGELOG.md
- app.py

## [1.18.0] - 2022-12-02

René Alejandro Rivas

### Added: 
- **sf_errors_handler()** to `salesforce_requests_service` to handle communication errors with salesforce's services

### Changed:
- Apps:
  - degree: communication errors handling with salesforce's services removed, unused code removed
  - equivalence_of_studies: communication errors handling with salesforce's services removed, unused code removed
  - reinstatement: communication errors handling with salesforce's services removed, unused code removed
- Constants: 
  - identifiers were renamed to add '_key' as a suffix
- Services:
  - **salesforce_requests_service**:
    - fetch_picklist() added
    - now fetch_picklist(), request_procedure_to_salesforce() and request_all_tickets_to_salesforce() use 
    sf_errors_handler() to handle communication errors
  - set_responses_service:
    - error_response(), successful_response_get_method(), successful_response_post_method() now return a tuple
    to send the http status code
  - logger now uses LOGGER_LEVEL environment variable to set the logs level
- Utils:
  - now studentData is decoded instead of the token's payload

### Deleted:
- `picklist_service`: fetch_picklist() was moved to `salesforce_requests_service` to use sf_errors_handler()
  
## [1.17.0] - 2022-12-01

René Alejandro Rivas

### Added:
  - **tickets_service**
### Changed:
- Apps:
  - All apps renamed to add '_app' sufix to them
  - **degree**: _record_types_repository dropped, get_successful_response used to send response
  - **tickets_app**: Full refactor of the `tickets_app`. Now consumes from tickets_service:
    - get_sf_tickets_url_with_record_types()
    - set_valid_tickets_array()
    - set_payments_request_body()
    - fetch_tickets_transaction_numbers()
    - set_trans_nums_to_tickets_list()
- Constants:
  - `degree_procedure` renamed to `degree_constants`
  - Some identifiers added to `identifiers_constants`
  - `ssces_constants`: accessTokenSecret deleted
- Services:
  - Now every http request logs the status code of the request
  - **cost_service**: Now costs_service performs request to payments service to fetch degree's costs
  - **picklist_service** Logs and errors handling added
  - **programs_service** Http request to programs service (from proxy service) added
  - **request_procedure_service**:
    - at request_procedure_to_salesforce() improved exceptions handling and error messages
    - at request_all_tickets_to_salesforce() improved exceptions handling and error messages
  - **set_responses_service**: 
    - get_successful_response() added to send successful responses
    - error_object() deleted (no longer in use)
  - **sf_core_service** Token type added to the response
  - 
- Utils:
  - **decoder**: Now token_decoder doesn't verify token's signature, also a bug fix added at rising error
### Deleted:
- costs_proxy_service (not needed)
- programs_proxy_service (not needed)
- salesforce_ula_constants (bad structure)

## [1.16.6] - 2022-11-16
Eduardo Izquierdo Rojas

### Changed:
Refactor handling modalities in degree service controller
Use of modality fetch record detail code
- apps/degree.py
- services/degree_service.py
- 
Set of properties depends on modality 
- services/set_servicio_fields.py

Update of collections for modality 'Escolarizada' and 'A Distancia'
- services/update_collections_service.py

Brief changes addition of logs
- services/request_procedure_service.py
- apps/equivalence_of_studies.py
- services/degree_record_types_service.py



## [1.16.5] - 2022-10-26
Eduardo Izquierdo Rojas

Moved acrom and label identifiers to mongo
- services/update_collections_service.py
- apps/degree.py
- services/degree_record_types_service.py            
- services/set_servicio_fields.py

## [1.16.5] - 2022-10-26
Eduardo Izquierdo Rojas

Deactivation of traditional degree
- apps/degree.py
- services/set_servicio_fields.py
- services/update_collections_service.py

## [1.16.4] - 2022-10-24
Eduardo Izquierdo Rojas

Delete programs of endpoint GET and POST
- apps/degree.py
- services/set_servicio_fields.py

Change in version 
- app.py
- CHANGELOG.md

## [1.16.3] - 2022-10-20
Eduardo Izquierdo Rojas

Correction bug and addition of exception for "Session expired or invalid"
- apps/degree.py
- apps/equivalence_of_studies.py
- apps/reinstatement.py
- apps/request_tickets.py

Change type of method in petition 
- services/programs_proxy_service.py
- services/programs_service.py




## [1.16.2] - 2022-10-05
Eduardo Izquierdo Rojas

### Changed:
Addition of variable environment to size in payload to send files
- OpenAPI/commons.py
- app.py
- constants/ssces_constants.py
- CHANGELOG.md

## [1.16.1] - 2022-09-14
Eduardo Izquierdo Rojas

### Changed:

Correction tests and addition of mocks to make tests
for modality online and schooled

- tests/commons.py
- tests/test_functions.py
- tests/test_get_request_all_procedures.py
- tests/test_post_degree.py
- tests/test_post_equivalence_of_studies.py
- tests/test_post_reinstatement.py



## [1.16.0] - 2022-09-14
Eduardo Izquierdo Rojas


### Changed: 
Modification of models openapi for request post
- OpenAPI/degree_openapi.py
  - OpenAPI/reinstatement_openapi.py

Addition of validation for get detail_code, record_type
- apps/equivalence_of_studies.py
  - apps/reinstatement.py
  - apps/degree.py

Deleted conditional the get error and addition request_tickets_procedure_to_salesforce()
-apps/request_tickets.py

Addition of constants and identifiers
- constants/degree_procedure.py
  - constants/identifiers_constants.py
  - constants/salesforce_ula_constants.py

Modification of set of fiels depends of madality
- services/set_servicio_fields.py

Addition of logs in methods
- services/degree_record_types_service.py

Addition fetch_degree_schooled_record_detail_code() to get detail_code,for degree schooled
- services/degree_service.py

update check_if_update_needed_in_degree_procedure_records() anda verified 
collecion degree schooled
- services/update_collections_service.py

Addtion of method request_tickets_procedure_to_salesforce()
- services/request_procedure_service.py

Update of tests       
- tests/commons.py
  - tests/test_get_request_all_procedures.py
  - tests/test_post_equivalence_of_studies.py
  - tests/test_post_reinstatement.py
  - tests/test_post_degree.py 
  - requirements.txt

## [1.15.0] - 2022-08-31
Eduardo Izquierdo Rojas

### Added
Modify of method "error_response()" to be able to handle exceptions properly,
respond and stop the flow of the request, if an error occurs

And Addition of "error_response_auth()" for the exclusive use 
of Authorization middleware to avoid circular decency
- services/set_responses_service.py

Change method "error_response()" by "error_response_auth()" 
in method "set_auth_error_response()" to avoid circular decency
- services/authorization_service.py

### Removed:
Removed conditionals to check for errors in requests in controllers
- apps/degree.py                                     
- apps/equivalence_of_studies.py                     
- apps/reinstatement.py                              
- apps/request_tickets.py 

### Changed: 
Added method "error_response()" now to return exception if there is an error
and stop the flow when making a request, in services

- services/fetch_keys_service.py
- services/request_procedure_service.py
- services/set_servicio_fields.py
- services/sf_core_service.py
- services/transaction_number_service.py

Brief modification in version
- CHANGELOG.md  
- app.py


## [1.14.17] - 2022-08-30

Eduardo Izquierdo Rojas

### Changed:
Remove of logs not need and correction 
in responses when the connection to Salesforce fails

- apps/degree.py
- apps/reinstatement.py
- services/update_collections_service.py

## [1.14.16] - 2022-08-26

Eduardo Izquierdo Rojas
### Changed:

Addition of param school in function "check_if_update_needed_in_degree_procedure_records"
- apps/degree.py
- services/degree_service.py
- services/update_collections_service.py

## [1.14.15] - 2022-08-26

Eduardo Izquierdo Rojas
### Changed:

Additon of logs in reinstatement service
- apps/reinstatement.py

## [1.14.14] - 2022-08-25

Eduardo Izquierdo Rojas

### Changed:
Refactor of function "get_sf_access_token()" where to add param school
for change between token that depends of school

- services/sf_core_service.py

Addition of param school in function get_sf_access_token(email, school) 
where is it used 
- function_procedure_service.py
- apps/request_tickets.py

Brief change in version of the API 
- app.py
- CHANGELOG.md

## [1.14.13] - 2022-08-19

Eduardo Izquierdo Rojas

### Changed:
## Service reinstatement
Correction in CommonRequestBody deleted fields 
- OpenAPI/commons.py   

Addtion of model and fields in ReinstatementRequestBody 
- OpenAPI/reinstatement_openapi.py
- apps/reinstatement.py

--------------------------
## Service degree

### Added
Addtion of Service to consume programs of 'permissions service'
- services/programs_proxy_service.py
- services/programs_service.py

Addition of methods 'get_programs_detail(), 
get_label_list_request_programs()' for get programs 

- apps/degree.py
- services/degree_record_types_service.py
- services/degree_service.py

Addition of constants, identifiers of 'permissions service'
- constants/identifiers_constants.py
- constants/services_urls.py

Addtion of field 'programTypeValue' for request body in degree
- OpenAPI/degree_openapi.py 


## [1.14.11] - 2022-08-03

Eduardo Izquierdo Rojas

### Changed:
Addition of validation "validate_size_in_file()" in field "fileBody" of Files(BaseModel)
to not allow files larger than 2 Mb  when making the post request, in files that are loaded

- OpenAPI/commons.py

Brief modification in file
- CHANGELOG.md 


## [1.14.0] - 2022-08-03

Eduardo Izquierdo Rojas

### Added
Addition of new fields for reinstatement service
  
  - countryOfBirth
  - countryOfPriorStudies 
  - schoolOfOrigin
  - street
  - number 
  - neighborhood
  - cp 
  - population
  - city
  - entity
  - schoolPhone
  - schoolEmail
  - startDatePreviousLevel
  - endDatePreviousLevel

Addition of fields in models openAPI, interfaces
- OpenAPI/commons.py
- interfaces/interfaces.py

Addtion of function "set_servicio_ula_added_fields()" for set fields 
- services/set_servicio_fields.py

Addition of  function "set_sf_date_format(date: str)" for format in date
to insert in saleforce
-utils/utilities.py

### Changed:
Addition of param "service_name" in function set_servicio_properties()
for identify which service it is

- apps/reinstatement.py
- apps/equivalence_of_studies.py


## [1.13.0] - 2022-07-27

René Alejandro Rivas

### Added
- error handling added at request_tickets.py
- degree service: validation of phoneNumber at request_body 
- 
### Changed:
- refactor done at request_tickets.py:
  - now it consumes record_types_ids just from one repository validating a field called recordTypeId
- matricula_not_found renamed to unavailable_option
- recordtypes_repository.py renamed to degree_repository.py
- record_types_service.py renamed to degree_record_types_service.py
- databese.py renamed to database.py

### Deleted:
- /database/databese2.py (not needed)

## [1.12.0] - 2022-07-07

René Alejandro Rivas

### Added: 

- Status__c and Etapa_UTC__c properties to Service interfaces to set Estado: 'Nuevo' in all tickets

### Changed: 

- Now interfaces inherit BaseModel class for a better security and error handling in the service object

## [1.11.0] - 2022-07-06

Eduardo Izquierdo Rojas

### Changed:

Adsition of label and acrom fields for request GET 
- apps/degree.py

- Refactor in request to saleforce to get tickects by means of matricula and records
- apps/request_tickets.py

brief addition of parameter
- services/update_collections_service.py


## [1.10.0] - 2022-06-20

René Alejandro Rivas

### Added:
- fetch_keys_service.py
  - to fetch keys from SS_Keys collection 
- identifiers_constants.py (to create SF 'servicio' object)
- interfaces.py
- keys_repository.py (to fetch SF record types ID)
- messages.py

### Changed:
- controllers and services now fetch email via student_data object
- set_servicio_fields.py
  - now uses interfaces to create "servicio object"
  - validation to get school and fill corresponding object
- equivalence_of_study and reinstatement controllers
  -  they now work both for UTC and ULA schools, using set_servicio_fields service
- SS_KEYS added collections_constants.py
- degree_service recieves student_data param instead of auth_header
- (to avoid decode token multiple times)
- repositories use constants collection names 

### deleted
- getEmail.py (not needed)

## [1.9.1] - 2022-06-20

Eduardo Izquierdo Rojas

### Added:
Addition of request to cost service
- services\costs_proxy_service.py
- services\costs_service.py

### Changed:
Addition  costs in request get degree
- apps\degree.py

Addition of URL COST SERVICE
- constants\services_urls.py

Brief modification, rename repositiry
- repositories\detail_codes_repository.py
- repositories\recordtypes_repository.py
- services\update_collections_service.py
- services\record_types_service.py
- services\degree_service.py
- utils\utilities.py

## [1.9.0] - 2022-05-25

Eduardo Izquierdo Rojas

### Added:
addition degree service
- apps/degree.py

addition of sales force constants url's of ULA
- constants/salesforce_ula_constants.py

Addition constants for degree service 
- constants/collections_constants.py 
- constants/degree_procedure.py

Addition of Open Api Swagger for degree service
-  OpenAPI/degree_openapi.py

addition of directory repositories and files, for connection 
with collections in mongodb
- repositories/detail_codes_resipository.py
- repositories/recordtypes_resipository.py

Addition of services for degree service
- services/degree_service.py
- services/picklist_proxy_service.py
- services/record_types_service.py
- services/sf_core_service.py
- services/update_collections_service.py

Addition file utilities in utils and functions for degree service 
- utils/utilities.py


### Changed:

addition on route: "degree/v1"
-  constants/ssces_constants.py

brief modification in the import of get_sf_access_token method
- apps/equivalence_of_studies.py
- apps/reinstatement.py
- apps/request_tickets.py

addition of request_to_sf_ula() for request services ULA
- services/request_procedure_service.py

addition of parameter code_detail_id in get_transaction_number()
- transaction_number_service.py

brief modification
- app.py


## [1.8.3] - 2022-02-15

Eduardo Izquierdo Rojas

### Added:
file to connection to mongodb:
- database/mongo/databese2.py

function of to save document in mongodb 
- services/env_variable_looger_service.py   

function to get email for logs 
- services/getEmail.py

### Changed:
Addition of email in logs     

- apps/equivalence_of_studies.py                     
- apps/reinstatement.py
- apps/request_tickets.py

Addition of verification variables environment, if not found to save in mongodb

- constants/services_urls.py

Addition of constants in file constants/ssces_constants.py, 
for function of to save variables in mongo:

- ENVIRONMENT
- URLDBREMOTE
- MYDB


## [1.8.2] - 2022-02-11

Eduardo Izquierdo Rojas

### Added:

- Tests for services SSCES, and directory of tests
- mocks of data commons tests/commons.py
- tests for request_all_procedures, tests/test_get_request_all_procedures.py
- tests for equivalence_of_studies, tests/test_post_equivalence_of_studies.py
- tests for test_post_reinstatement, tests/test_post_reinstatement.py

## [1.8.1] - 2022-02-08
Ren� Alejandro Rivas

### Changed:
- Validation for null transaction Numbers
  - instead of "null" it searches for "-1" values
- logs improved

## [1.8.0] - 2022-02-01
Ren� Alejandro Rivas

### Added:
- tickets length validation: If tickets array returns empty from salesforce, then payments service is not requested.
- tickets date validation: Tickets with status of "Nuevo" and date of more than 5 days of created are ignored.

### Changed:
- Services URLs logged


## [1.7.0] - 2022-01-21
Ren� Alejandro Rivas

### Added:
- 404 error response in case **payments** service fails.
  - status.info message added that will be displayed to student

### Changed:
- **periodCode** retrieved from accesstoken and sent to payments service to request **equivalence of studies**
- **service-id** is not required anymore in payments body to request all tickets transaction numbers.
- bugfix in `transaction_number_service.py` when access token has expired.


## [1.6.0] - 2022-01-14
Ren� Alejandro Rivas

### Added:
- `transaction_number_service.py`. This service communicates with **payments** service in order to retrieve the _transactionNumber_ needed to make the payment.
- 'sf_core_unavailable', 'sf_servicios_escolares_unavailable', 'payments_unavailable', 'communication_error' constants for error handling.
- `external_services_constants.py` file added for constants needed related to third party services.

### Changed:
- `equivalence_of_studies.py` app now is able to use `transaction_number_service.py` in order to retrieve transactionNumber.
- `request_tickets.py` now also can consume **payments** service in order to retrieve all *transactionNumber*s from all of the tickets.
- currently a _transactionNumber_ dummy is sent both in _equivalence_of_studies_ and in _request_tickets_ because the service of 'paymens' is not available.
- POST endpoints now return a '201 Created' status code
- now all of the imports explicitly set all the functions or constants that are importing.
- HOST variable set to '0.0.0.0'
- PORT variable set to 80
- SSCES_HOST renamed to SSCES
- improved error handling 


## [1.5.0] - 2022-01-03
Ren� Alejandro Rivas

### Added:
- `decoder.py` utility for decoding and handling errors regarding decoding access token

### Changed:
- `set_servicio_fields.py` now uses `decoder.py` utility for decoding access token.
- "matricula" is no longer hardcoded, instead it is retrieved (in all apps) from access token.
- `request_tickets.py` retrieves 'matricula' from access token using `decoder.py` utility.
- "_chargeAccepted_" param in requestBody no longer a required param.

### Removed:
- "MATRICULA" constant. 

## [1.4.0] - 2021-12-30
Ren� Alejandro Rivas

### Added:
- "SF-ServiciosEscolares" URL version 2
- some logs info

### Changed:
- Now it is consumed version 2 of "SF-ServiciosEscolares". Needed changes were done.

### Deleted:
- "SF-ServiciosEscolares" URL version 1

## [1.3.0] - 2021-12-30
Ren� Alejandro Rivas

### Added:
- app: POST for 'Reincorporaci�n' procedure
- exception handling
- final user messages
- services: 
  - request_procedure
  - set_responses
  - authorization_service: set_auth_error_response()
- security parameter to all endpoint decorators

### Changed:
  - POST routes consume request_procedure and set_responses service.
  - thinner controllers
  - documentation updated

## [1.2.1] - 2021-12-29
Ren� Alejandro Rivas

### Added:
- routes file with all the routes of the application
- .gitignore file

### Changed:
- Authorization middleware now skips all validations if route not in one of the application routes

### Removed:
- documentation_urls files because it's no longer needed

## [1.2.0] - 2021-12-28
Ren� Alejandro Rivas

### Added:
- documentation_urls file with documentation_urls array. When accessing to one of these URLs, Authorization middleware will not take effect.
- more logs

### Changed:
- Authorization middleware activated. It checks if URL is in documentation_urls. In that case it doesn't continue validating headers.

### Removed:
- All "before_request" functions in controllers. No longer needed because of the Authorization middleware.
- checkAuthorization() in authorization_service. Also no longer needed.

## [1.1.0] - 2021-12-27
Ren� Alejandro Rivas

### Added:
- "flask-openapi3" package to create swagger documentation using classes inside the controllers
- OpenAPI directory with swagger documentation
- "pydantic" package to validate params schemas
- POST endpoint for request "Equivalence of studies" to salesforce
- "copy" package to create deep copies.

### Changed:
- every endpoint answers with a deepcopy of "sscesResponse" object
- fixed 403 expired token status code response

### Removed:
- "flask-swagger-ui" package
- static directory
- swagger files

## [1.0.0] - 2021-12-20
Ren� Alejandro Rivas

### Added:
- Flask microservice created
- main app.py file created
- Services:
  - Logger
  - Authorization
- Constants
  - SSCES constants
  - servicesUrls
- Apps
  - credential
  - requestAllProcedures
- Database connection
- docker files
- pipeline file
- config file