from typing import Type, TypeVar

T = TypeVar('T')


class ValueType:
    _type = None
    _default = None

    def __init__(self, start_value: T = None):
        self.value = start_value or self._default

    @property
    def value(self) -> T:
        return self.__value

    @value.setter
    def value(self, value: T) -> None:
        if type(value) != self._type:
            raise ValueError

        self.__value = value

    def __str__(self):
        return str(self.value)


class Integer(ValueType):
    _type = int
    _default = 0


class Float(ValueType):
    _type = float
    _default = 0.0


class Array:
    def __init__(self, max_length: int, cell: Type[ValueType]):
        self.max_length = max_length
        self.cell: Type[ValueType] = cell
        self.lst = [self.cell() for _ in range(max_length)]

    def is_valid_index(self, idx: int) -> bool:
        return type(idx) == int and 0 <= idx <= (self.max_length - 1)

    def __getitem__(self, item):
        if not self.is_valid_index(item):
            raise IndexError
        return self.lst[item].value

    def __setitem__(self, key, value):
        if not self.is_valid_index(key):
            raise IndexError
        self.lst[key].value = value

    def __str__(self):
        return ' '.join(map(str, self.lst))
