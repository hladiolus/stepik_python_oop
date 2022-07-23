from functools import singledispatchmethod
from typing import Tuple, overload


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_coords(self) -> Tuple[int, int]:
        return self.__x, self.__y


class Rectangle:
    def __init__(self, *args: Point | int, **kwargs):
        if len(args) == 2 and all(map(lambda x: isinstance(x, Point), *args)):
            self.__sp, self.__ep = args
        elif len(args) == 4 and all(map(lambda x: isinstance(x, int), *args)):
            self.__sp, self.__ep = Point(*args[:2]), Point(*args[2:])

    def set_coords(self, sp: Point, ep: Point) -> None:
        self.__sp = sp
        self.__ep = ep

    def get_coords(self) -> Tuple[Point, Point]:
        return self.__sp, self.__ep

    def draw(self):
        print(f'Прямоугольник с координатами: {self.__sp.get_coords()} {self.__ep.get_coords()}')


rect = Rectangle(0, 0, 20, 34)



