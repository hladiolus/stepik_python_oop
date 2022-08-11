import sys


class BookStudy:
    def __init__(self, name: str, author: str, year: int):
        self.name = name
        self.author = author
        self.year = year

    def __hash__(self):
        return hash((self.name.lower(), self.author.lower()))


lst_in = list(map(str.strip, sys.stdin.readlines()))
lst_bs = []

for line in lst_in:
    name, author, year = line.split('; ')
    lst_bs.append(BookStudy(name, author, int(year)))

_hashes = []
unique_books = 0

for book in lst_bs:
    if h := hash(book) not in _hashes:
        _hashes.append(h)
        unique_books += 1
