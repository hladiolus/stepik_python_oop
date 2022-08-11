from typing import Union


class Person:
    def __init__(self, fio: str, job: str, old: int,
                 salary: Union[int, float], year_job: int):
        self.fio = fio
        self.job = job
        self.old = old
        self.salary = salary
        self.year_job = year_job
        self._current_item = 0
        self._keys = list(self.__dict__.keys())

    def is_valid_index(self, idx: int) -> bool:
        return isinstance(idx, int) and 0 <= idx < 5

    def __getitem__(self, item):
        if not self.is_valid_index(item):
            raise IndexError
        return self.__dict__[self._keys[item]]

    def __setitem__(self, key, value):
        if not self.is_valid_index(key):
            raise IndexError
        self.__dict__[self._keys[key]] = value

    def __next__(self):
        if self._current_item == 5:
            raise StopIteration
        self._current_item += 1
        return self.__getitem__(self._current_item - 1)

    def __iter__(self):
        self._current_item = 0
        return self
