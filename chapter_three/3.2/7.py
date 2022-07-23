class HandlerGET:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        if args[0].get('method', 'GET') != "GET":
            return None
        return f'GET: {self.func(*args, **kwargs)}'
