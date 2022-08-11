from typing import Union


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10000

    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    @property
    def a(self) -> int:
        return self.__a

    @a.setter
    def a(self, value: int) -> None:
        if self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
            self.__a = value

    @property
    def b(self) -> int:
        return self.__b

    @b.setter
    def b(self, value: int) -> None:
        if self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
            self.__b = value

    @property
    def c(self) -> int:
        return self.__c

    @c.setter
    def c(self, value: int) -> None:
        if self.MIN_DIMENSION <= value <= self.MAX_DIMENSION:
            self.__c = value

    def volume(self):
        return self.a * self.b * self.c

    def __le__(self, other):
        return self.volume() <= other.volume()

    def __lt__(self, other):
        return self.volume() < other.volume()


class ShopItem:
    def __init__(self, name: str, price: Union[int, float], dim: Dimensions):
        self.name = name
        self.price = price
        self.dim = dim


lst_shop = [
    ShopItem('кеды', 1024, Dimensions(40, 30, 120)),
    ShopItem('зонт', 500.24, Dimensions(10, 20, 50)),
    ShopItem('холодильник', 40000, Dimensions(2000, 600, 500)),
    ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))
]

lst_shop_sorted = sorted(lst_shop[:], key=lambda x: x.dim.volume())