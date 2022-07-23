from typing import Optional


class Car:
    def __init__(self):
        self.__model: Optional[str] = None

    @property
    def model(self) -> Optional[str]:
        return self.__model

    @model.setter
    def model(self, value: Optional[str]) -> None:
        if isinstance(value, str) and 2 <= len(value) <= 100:
            self.__model = value

    @model.deleter
    def model(self) -> None:
        del self.__model
