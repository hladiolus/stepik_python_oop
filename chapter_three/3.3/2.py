import sys


class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.__title = title
        self.__author = author
        self.__pages = pages

    def __str__(self):
        return f"Книга: {self.__title}; {self.__author}; {self.__pages}"


title, author, pages = list(map(str.strip, sys.stdin.readlines()))
book = Book(title, author, int(pages))
