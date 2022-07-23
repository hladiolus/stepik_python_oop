from typing import List


class Thing:
    def __init__(self, name: str, weight: float | int):
        self.name = name
        self.weight = weight


class Bag:
    def __init__(self, max_weight: float | int):
        self.max_weight = max_weight
        self.__things: List[Thing] = []
        self.__total_weight = 0

    @property
    def things(self) -> List[Thing]:
        return self.__things

    def add_thing(self, thing: Thing) -> None:
        if self.__total_weight + thing.weight <= self.max_weight:
            self.__total_weight += thing.weight

    def remove_thing(self, indx: int) -> None:
        self.__total_weight -= self.__things[indx].weight
        self.__things.pop(indx)

    def get_total_weight(self):
        return self.__total_weight
