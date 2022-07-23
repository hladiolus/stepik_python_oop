from typing import List
from math import sqrt


class LineTo:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def dist(self, other: 'LineTo') -> float:
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


class PathLines:
    def __init__(self, *lines):
        self.__path: List[LineTo] = [LineTo(0, 0)]

        for line in lines:
            self.add_line(line)

    def get_path(self) -> List[LineTo]:
        return self.__path

    def get_length(self) -> float:
        length = 0
        for idx, line in enumerate(self.__path[1:]):
            length += line.dist(self.__path[idx])
        return length

    def add_line(self, line: LineTo) -> None:
        if isinstance(line, LineTo):
            self.__path.append(line)
