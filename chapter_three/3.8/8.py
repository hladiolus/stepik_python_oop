from typing import Tuple, Union


class Cell:
    def __init__(self):
        self.is_free = True
        self.value = 0

    def __bool__(self):
        return self.is_free


class TicTacToe:
    def __init__(self):
        self.pole: Tuple[Tuple[Cell, ...], ...] = self.gen_pole()

    def gen_pole(self) -> Tuple[Tuple[Cell, ...], ...]:
        return tuple([tuple([Cell() for _ in '...']) for _ in '...'])

    def clear(self):
        self.pole = self.gen_pole()

    def is_valid_index(self, idx: Union[Tuple[int, int], Tuple[slice, int], Tuple[int, slice]]) -> bool:
        return isinstance(idx, tuple) and 0 <= idx[0] < 3 and 0 <= idx[1] < 3

    def __getitem__(self, item: Union[Tuple[int, int], Tuple[slice, int], Tuple[int, slice]]) \
            -> Union[int, Tuple[Cell, ...]]:
        if isinstance(item[0], int):
            if isinstance(item[1], int):
                return self.pole[item[0]][item[1]].value
            if isinstance(item[1], slice):
                return tuple([self.pole[item[0]][i].value for i in range(3)])
        if isinstance(item[0], slice):
            return tuple([self.pole[i][item[1]].value for i in range(3)])
        raise IndexError

    def __setitem__(self, key, value):
        if not self.is_valid_index(key):
            raise IndexError
        cell: Cell = self.pole[key[0]][key[1]]
        if not cell.is_free:
            raise ValueError
        cell.value = value
