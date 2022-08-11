from typing import Union, List

T = Union[int, float]


class Thing:
    def __init__(self, name: str, weight: T):
        self.name = name
        self.weight = weight


class Bag:
    def __init__(self, max_weight: T):
        self.max_weight = max_weight
        self.things: List[Thing] = []
        self.current_weight = 0

    def add_thing(self, thing: Thing) -> None:
        if self.current_weight + thing.weight > self.max_weight:
            raise ValueError
        self.things.append(thing)
        self.current_weight += thing.weight

    def is_valid_index(self, idx: int) -> bool:
        return isinstance(idx, int) and idx < len(self.things)

    def __getitem__(self, item):
        if not self.is_valid_index(item):
            raise IndexError
        return self.things[item]

    def __setitem__(self, key, value):
        if not self.is_valid_index(key):
            raise IndexError
        if not isinstance(value, Thing):
            raise ValueError
        new_weight = self.current_weight - self.things[key].weight + value.weight
        if new_weight > self.max_weight:
            raise ValueError
        self.things[key] = value
        self.current_weight = new_weight

    def __delitem__(self, key):
        if not self.is_valid_index(key):
            raise IndexError
        self.current_weight -= self.things[key].weight
        del self.things[key]
