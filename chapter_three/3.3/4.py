from re import split as resplit
from typing import List


class WordString:
    def __init__(self, string: str = ""):
        self.__splitted: List[str] = []
        self.string = string

    @property
    def string(self) -> str:
        return self.__string
    
    @string.setter
    def string(self, value: str) -> None:
        self.__string = value
        self.__splitted = resplit(r' +', value.strip())

    def __len__(self):
        return len(self.__splitted)

    def __call__(self, *args, **kwargs):
        return self.__splitted[args[0]]


words = WordString()
words.string = "1 2 3    4 5 6 7"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")