from typing import Union


class Circle:
    def __init__(self, x: Union[int, float], y: Union[int, float], radius: Union[int, float]):
        self.x = x
        self.y = y
        self.radius = radius

    @property
    def x(self) -> Union[int, float]:
        return self.__x

    @x.setter
    def x(self, value: Union[int, float]) -> None:
        if isinstance(value, (int, float)):
            self.__x = value
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    @property
    def y(self) -> Union[int, float]:
        return self.__y

    @y.setter
    def y(self, value: Union[int, float]) -> None:
        if isinstance(value, (int, float)):
            self.__y = value
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    @property
    def radius(self) -> Union[int, float]:
        return self.__radius

    @radius.setter
    def radius(self, value: Union[int, float]) -> None:
        if isinstance(value, (int, float)):
            self.__radius = value
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __setattr__(self, key, value):
        if key == 'radius' and value <= 0:
            pass
        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False
