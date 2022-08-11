from typing import Union

T = Union[int, float]


class Triangle:
    def __init__(self, a: T, b: T, c: T):
        if not all(map(lambda x: type(x) in (int, float) and x > 0, (a, b, c))):
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        if not sum([a, b, c]) - max([a, b, c]) > max([a, b, c]):
            raise ValueError("с указанными длинами нельзя образовать треугольник")
        self.a, self.b, self.c = a, b, c

    def __len__(self) -> int:
        return int(self.a + self.b + self.c)

    def __call__(self) -> float:
        p = len(self) / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c))**.5
