from functools import wraps

from flask import request, abort
from pydantic import ValidationError


def body(dto_class):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                data = request.get_json()
                dto = dto_class(**data)
                return func(dto=dto, *args, **kwargs)
            except ValidationError as e:
                abort(400, {'message': 'custom error message to appear in body'})

        return wrapper

    return decorator
