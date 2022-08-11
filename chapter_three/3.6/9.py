from typing import Union

T = Union[int, float]


class Dimensions:
    def __init__(self, a: T, b: T, c: T):
        if not all(map(lambda x: type(x) in (int, float) and x > 0, (a, b, c))):
            raise ValueError("габаритные размеры должны быть положительными числами")
        self.a = a
        self.b = b
        self.c = c

    def __hash__(self) -> int:
        return hash((self.a, self.b, self.c))


lst_dims = sorted([Dimensions(*map(float, args.split())) for args in input().split(';')],
                  key=lambda x: hash(x))
