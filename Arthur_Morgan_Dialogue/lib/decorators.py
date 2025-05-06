from functools import wraps

from django.shortcuts import redirect


def view(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        response = view_func(request, *args, **kwargs)
        return response
    return wrapper