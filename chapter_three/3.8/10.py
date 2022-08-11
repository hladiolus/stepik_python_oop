from typing import Tuple, Dict, TypeVar

T = TypeVar('T')


class Cell:
    def __init__(self, value):
        self.value = value


class SparseTable:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.table: Dict[Tuple[int, int], T] = {}

    def add_data(self, row: int, col: int, data: T):
        if not self.is_valid_index(row, col) or self.index_in_table(row, col):
            raise IndexError
        self._add_data(row, col, data)

    def _add_data(self, row: int, col: int, data: T):
        self.table[(row, col)] = data
        self.rows = max(self.rows, row + 1)
        self.cols = max(self.cols, col + 1)

    def is_valid_index(self, row: int, col: int) -> bool:
        return isinstance(row, int) and isinstance(col, int) and \
               row >= 0 and col >= 0

    def index_in_table(self, row, col):
        return (row, col) in self.table

    def remove_data(self, row: int, col: int) -> None:
        if not self.is_valid_index(row, col) or not self.index_in_table(row, col):
            raise IndexError
        del self.table[(row, col)]
        self.rows, self.cols = 0, 0
        for k in self.table.keys():
            self.rows = max(self.rows, k[0] + 1)
            self.cols = max(self.cols, k[1] + 1)

    def __getitem__(self, item):
        if not self.is_valid_index(*item):
            raise IndexError
        if not self.index_in_table(*item):
            raise ValueError
        return self.table[(item[0], item[1])]

    def __setitem__(self, key, value):
        if not self.is_valid_index(*key):
            raise IndexError
        if key in self.table:
            self.table[key] = value
        else:
            self._add_data(*key, value)
