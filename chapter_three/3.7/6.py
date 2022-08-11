from typing import Union

T = Union[int, float]


class Line:
    def __init__(self, x1: T, y1: T, x2: T, y2: T):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __setattr__(self, key, value):
        if type(value) not in (int, float):
            raise ValueError
        object.__setattr__(self, key, value)

    def __len__(self) -> int:
        return int(((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)**.5)
