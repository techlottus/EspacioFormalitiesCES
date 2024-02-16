from datetime import datetime
from services.logger_service import logger


def check_date_changed(date_input: datetime):
    date_today = datetime.now()
    day_current = date_today.day
    month_current = date_today.month
    year_current = date_today.year

    if date_input.day != day_current or date_input.month != month_current or date_input.year != year_current:
        return True
    else:
        return False


def create_id_with_prefix(record_type_name: str, input_string: str):
    list_words = input_string.upper().split(" ")
    identifier = ''
    for word in list_words:
        identifier += word[0] + str(len(word))

    return get_prefix(record_type_name) + identifier


def get_prefix(record_type_name: str):
    return record_type_name[0:3].upper()


def log_not_defined_env_var(var_name: str):
    logger.warning(f"{var_name} environment variable is not defined.")


def set_sf_date_format(date: str):
    logger.debug(f"set_sf_date_format() accessed")
    date_array = date.split('/')
    sf_format_date = date_array[2] + '-' + date_array[1] + '-' + date_array[0]
    logger.debug(f"Salesforce format date:{sf_format_date}")
    return sf_format_date
