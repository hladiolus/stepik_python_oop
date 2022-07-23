from typing import List, Optional, Tuple
import time


class Filter:
    def __init__(self, date: int):
        self.date = date

    def __setattr__(self, key, value):
        object.__setattr__(self, key, getattr(self, key, value))


class Mechanical(Filter):
    pass


class Aragon(Filter):
    pass


class Calcium(Filter):
    pass


class GeyserClassic:
    MAX_DATE_FILTER = 100
    __slots_filter = {1: Mechanical, 2: Aragon, 3: Calcium}

    def __init__(self):
        self.filters: List[Optional[Filter]] = [None, None, None]

    def add_filter(self, slot_num: int, filter: Filter) -> None:
        if 1 <= slot_num <= 3:
            if not self.filters[slot_num - 1] and \
                    isinstance(filter, self.__slots_filter[slot_num]):
                self.filters[slot_num - 1] = filter

    def remove_filter(self, slot_num: int) -> None:
        if 1 <= slot_num <= 3:
            self.filters[slot_num - 1] = None

    def get_filters(self) -> Tuple[Optional[Filter]]:
        return tuple(self.filters)

    def water_on(self) -> bool:
        return None not in self.filters and \
               all(map(lambda filter: 0 <= time.time() - filter.date <= self.MAX_DATE_FILTER, self.filters))
