from typing import Union, Tuple, List

T = Union[int, float]


class Track:
    def __init__(self, start_x: T, start_y: T):
        self.start_x = start_x
        self.start_y = start_y
        self.points: List[List[Union[Tuple[T, T], T]]] = []

    def add_point(self, x: T, y: T, speed: T) -> None:
        self.points.append([(x, y), speed])

    def is_valid_key(self, key: int):
        return isinstance(key, int) and 0 <= key <= (len(self.points) - 1)

    def __getitem__(self, item) -> List[Union[Tuple[T, T], T]]:
        if not self.is_valid_key(item):
            raise IndexError

        return self.points[item]

    def __setitem__(self, key, value):
        if not self.is_valid_key(key):
            raise IndexError

        self.points[key][1] = value
