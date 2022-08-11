from typing import Union, Optional, List


class Item:
    def __init__(self, name: str, money: Union[int, float]):
        self.name = name
        self.money = money

    def __add__(self, other) -> int:
        if isinstance(other, Item):
            other = other.money
        return self.money + other

    def __radd__(self, other):
        return self.__add__(other)


class Budget:
    def __init__(self):
        self.items: List[Optional[Item]] = []

    def add_item(self, it: Item) -> None:
        self.items.append(it)

    def remove_item(self, indx: int) -> None:
        if len(self.items) > indx:
            self.items.pop(indx)

    def get_items(self) -> List[Optional[Item]]:
        return self.items
