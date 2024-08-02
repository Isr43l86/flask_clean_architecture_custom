from functools import wraps

from flask import request
from pydantic import ValidationError

from src.exceptions import PydanticValidationException


def body(dto_class):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                data = request.get_json()
                dto = dto_class(**data)
                return func(dto=dto, *args, **kwargs)
            except ValidationError as e:
                errors_list = []
                for error in e.errors():
                    new_error = {
                        'type': error['type'],
                        'message': error['msg'],
                        'missing': error['loc'],
                        'url': error['url']
                    }
                    errors_list.append(new_error)
                raise PydanticValidationException(str(errors_list), 400)

        return wrapper

    return decorator
