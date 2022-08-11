from typing import Optional, List


class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year


class Lib:
    def __init__(self):
        self.book_list: List[Optional[Book]] = []
        self._len: int = 0

    def check_type(self, value):
        if not isinstance(value, Book):
            raise ValueError

    def __add__(self, other):
        self.check_type(other)
        self.book_list.append(other)
        self._len += 1
        return self

    def __sub__(self, other):
        if type(other) == int and len(self.book_list) > other:
            self.book_list.pop(other)
            self._len -= 1
        else:
            self.check_type(other)
            self.book_list.remove(other)
            self._len -= 1
        return self

    def __len__(self):
        return len(self.book_list)
