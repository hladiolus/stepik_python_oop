from typing import Optional


class Book:
    def __init__(self, author: str, title: str, price: int):
        self.__author: Optional[str] = None
        self.__price: Optional[int] = None
        self.__title: Optional[str] = None

        self.set_title(title)
        self.set_author(author)
        self.set_price(price)

    def set_title(self, title: str) -> None:
        self.__title = title

    def get_title(self) -> str:
        return self.__title

    def set_author(self, author: str) -> None:
        self.__author = author

    def get_author(self) -> str:
        return self.__author

    def set_price(self, price: int) -> None:
        self.__price = price

    def get_price(self) -> int:
        return self.__price
