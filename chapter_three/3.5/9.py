from typing import Union
from functools import total_ordering


@total_ordering
class Body:
    def __init__(self, name: str, ro: Union[int, float], volume: Union[int, float]):
        self.name = name
        self.ro = ro
        self.volume = volume

    def get_weight(self):
        return self.ro * self.volume

    def __eq__(self, other: Union['Body', int]):
        if isinstance(other, Body):
            return self.get_weight() == other.get_weight()
        elif isinstance(other, int):
            return self.get_weight() == other

    def __lt__(self, other):
        if isinstance(other, Body):
            return self.get_weight() < other.get_weight()
        elif isinstance(other, int):
            return self.get_weight() < other
