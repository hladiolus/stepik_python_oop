from typing import Callable


class RenderDigit:
    def __call__(self, *args, **kwargs):
        try:
            return int(args[0])
        except ValueError:
            return None


class InputValues:
    def __init__(self, render: RenderDigit):
        self.render: RenderDigit = render

    def __call__(self, func: Callable):
        def wrapper(*args, **kwargs):
            return [self.render(i) for i in func().split(' ')]
        return wrapper


render = RenderDigit()


@InputValues(render=render)
def input_dg():
    return input()


res = input_dg()
print(res)