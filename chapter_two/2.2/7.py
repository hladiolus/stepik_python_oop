from math import pow


class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x: int | float = 0, y: int | float = 0):
        self.x = 0
        self.y = 0

        self.x = x
        self.y = y

    @property
    def x(self) -> int | float:
        return self.__x

    @x.setter
    def x(self, value: int | float) -> None:
        if isinstance(value, (int, float)) and self.MIN_COORD <= value <= self.MAX_COORD:
            self.__x = value

    @property
    def y(self) -> int | float:
        return self.__y

    @y.setter
    def y(self, value: int | float) -> None:
        if isinstance(value, (int, float)) and self.MIN_COORD <= value <= self.MAX_COORD:
            self.__y = value

    @staticmethod
    def norm2(vector: 'RadiusVector2D') -> float:
        return pow(vector.x, 2) + pow(vector.y, 2)
