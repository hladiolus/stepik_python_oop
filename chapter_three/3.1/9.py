from typing import Union


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    def __init__(self, a: Union[int, float], b: Union[int, float], c: Union[int, float]):
        self.a = a
        self.b = b
        self.c = c

    @property
    def a(self) -> Union[int, float]:
        return self.__a

    @a.setter
    def a(self, value: Union[int, float]) -> None:
        self.__a = value

    @property
    def b(self) -> Union[int, float]:
        return self.__b

    @b.setter
    def b(self, value: Union[int, float]) -> None:
        self.__b = value

    @property
    def c(self) -> Union[int, float]:
        return self.__c

    @c.setter
    def c(self, value: Union[int, float]) -> None:
        self.__c = value

    def __setattr__(self, key, value):
        if key in ['MIN_DIMENSION', 'MAX_DIMENSION']:
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        if key in ['a', 'b', 'c']:
            if self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
                object.__setattr__(self, key, value)
        else:
            object.__setattr__(self, key, value)
