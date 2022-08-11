from typing import TypeVar, Optional, List, Union

T = TypeVar("T")


class ListMath:
    def __init__(self, lst: Optional[List[T]] = None):
        if not lst:
            lst = []
        self.lst_math: List[Union[int, float]] = [
            i for i in lst if type(i) == int or type(i) == float
        ]

    @staticmethod
    def check_type(other):
        if type(other) not in (int, float):
            raise TypeError

    def __add__(self, other):
        self.check_type(other)
        return ListMath([i + other for i in self.lst_math])

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        self.check_type(other)
        self.lst_math = [i + other for i in self.lst_math]
        return self

    def __sub__(self, other):
        self.check_type(other)
        return ListMath([i - other for i in self.lst_math])

    def __rsub__(self, other):
        self.check_type(other)
        return ListMath([other - i for i in self.lst_math])

    def __isub__(self, other):
        self.check_type(other)
        self.lst_math = [i - other for i in self.lst_math]
        return self

    def __mul__(self, other):
        self.check_type(other)
        return ListMath([i * other for i in self.lst_math])

    def __rmul__(self, other):
        return self.__mul__(other)

    def __imul__(self, other):
        self.check_type(other)
        self.lst_math = [i * other for i in self.lst_math]
        return self

    def __truediv__(self, other):
        self.check_type(other)
        return ListMath([i / other for i in self.lst_math])

    def __rtruediv__(self, other):
        self.check_type(other)
        return ListMath([1/i for i in self.lst_math])

    def __itruediv__(self, other):
        self.check_type(other)
        self.lst_math = [i / other for i in self.lst_math]
        return self
