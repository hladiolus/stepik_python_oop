from typing import Callable


class InputDigits:
    def __init__(self, func: Callable):
        self.func = func

    def __call__(self, *args, **kwargs):
        return [int(i) for i in self.func().split(' ')]


@InputDigits
def input_dg():
    return input()

res = input_dg()
