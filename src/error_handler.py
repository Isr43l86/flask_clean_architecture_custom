import ast
import logging
from typing import Dict

from flask import jsonify
from werkzeug.exceptions import HTTPException

from .exceptions import ClientException, ApiException, PydanticValidationException, CustomError

logger = logging.getLogger(__name__)


def setup_error_handler(app):
    """
    Function that will register all the specified error handlers for the app
    """

    def create_error_response(error_message, status_code: int = 400):

        # Remove the default 404 not found message if it exists
        if not isinstance(error_message, Dict):
            error_message = error_message.replace("404 Not Found: ", '')

        response = jsonify({"error_message": error_message})
        response.status_code = status_code
        return response

    def error_handler(error):
        logger.error("exception of type {} occurred".format(type(error)))
        logger.exception(error)

        if isinstance(error, HTTPException):
            return create_error_response(str(error), error.code)
        elif isinstance(error, ClientException):
            return create_error_response(
                "Currently a dependent service is not available, "
                "please try again later", 503
            )
        elif isinstance(error, PydanticValidationException):
            errors_dict = ast.literal_eval(error.error_message)
            return errors_dict, error.status_code
        elif isinstance(error, CustomError):
            return create_error_response(error.error_message, error.status_code)
        elif isinstance(error, ApiException):
            return create_error_response(
                error.error_message, error.status_code
            )
        else:
            # Internal error happened that was unknown
            return "Internal server error", 500

    app.errorhandler(Exception)(error_handler)
    return app
