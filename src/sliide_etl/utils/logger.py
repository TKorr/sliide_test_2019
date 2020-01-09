"""
Logging module
"""
import logging


def set_logger():
    config_format = (
        "{"
        "'asc_time':'%(asctime)s',"
        "'level_name':'%(levelname)s',"
        "'level_no':'%(levelno)s',"
        "'message':'%(message)s',"
        "'file_name':'%(filename)s',"
        "'module':'%(module)s',"
        "'function_name':'%(funcName)s',"
        "'line_number':'%(lineno)d',"
        "'path_name':'%(pathname)s'"
        "}"
    )
    # create logger
    LOGGER = logging.getLogger(__name__)
    if not LOGGER.handlers:
        LOGGER.setLevel(logging.INFO)
        # create console handler
        CONSOLE_LOGGER = logging.StreamHandler()
        CONSOLE_LOGGER.setLevel(logging.INFO)
        # create formatter and add it to the handlers
        FORMATTER = logging.Formatter(config_format)
        CONSOLE_LOGGER.setFormatter(FORMATTER)
        # add the handlers to the logger
        LOGGER.addHandler(CONSOLE_LOGGER)

    return LOGGER
