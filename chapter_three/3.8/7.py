from typing import Union, List

T = Union[int, float]


class RadiusVector:
    def __init__(self, *coords):
        self.coords: List[T] = list(coords)

    def __getitem__(self, item):
        if isinstance(item, slice):
            return tuple(self.coords[item])
        if isinstance(item, int):
            return self.coords[item]

    def __setitem__(self, key, value):
        if isinstance(key, (int, slice)):
            self.coords[key] = value


v = RadiusVector(1, 1, 1, 1)
print(v[1]) # 1
v[:] = 1, 2, 3, 4
print(v[2]) # 3
print(v[1:]) # (2, 3, 4)
print(v[::2])
v[0] = 10.5