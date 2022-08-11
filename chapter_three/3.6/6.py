from typing import TypeVar
import sys


T = TypeVar("T", int, float)


class ShopItem:
    def __init__(self, name: str, weight: T, price: T):
        self.name = name
        self.weight = weight
        self.price = price

    def __eq__(self, other: 'ShopItem') -> bool:
        return self.__hash__() == other.__hash__()

    def __hash__(self) -> int:
        return hash((self.name.lower(), self.weight, self.price))


lst_in = list(map(str.strip, sys.stdin.readlines()))  # список lst_in в программе не менять!

shop_items = {}

for i in lst_in:
    name, args = i.split(':')
    obj = ShopItem(name, *map(float, args.strip().split()))
    shop_items[obj] = [obj, shop_items.get(obj, [None, 0])[1] + 1]
