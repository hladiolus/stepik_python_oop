from typing import Callable, Tuple


class Handler:
    def __init__(self, methods: Tuple[str, ...] = ('GET', )):
        self.methods = methods

    def __call__(self, func: Callable):
        def wrapper(request, *args, **kwargs):
            method = request.get('method', 'GET')
            if method not in self.methods:
                return None
            return self.__getattribute__(method.lower())(func, request, *args)
        return wrapper

    def get(self, func, request, *args, **kwargs) -> str:
        return f'GET: {func(request)}'

    def post(self, func, request, *args, **kwargs) -> str:
        return f'POST: {func(request)}'
