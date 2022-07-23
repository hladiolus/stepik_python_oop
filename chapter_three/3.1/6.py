from typing import List


class Exhibit:
    to_change = None

    def __init__(self, name: str, to_change: str, descr: str):
        self.name = name
        self.to_change = to_change
        self.descr = descr

    def __setattr__(self, key, value):
        if key == 'to_change':
            key = self.to_change
        object.__setattr__(self, key, value)


class Picture(Exhibit):
    to_change = 'author'


class Mummies(Exhibit):
    to_change = 'location'


class Papyri(Exhibit):
    to_change = 'date'


class Museum:
    def __init__(self, name: str):
        self.name = name
        self.exhibits: List[Exhibit] = []

    def add_exhibit(self, obj: Exhibit) -> None:
        if isinstance(obj, Exhibit):
            self.exhibits.append(obj)

    def remove_exhibit(self, obj: Exhibit) -> None:
        self.exhibits.remove(obj)

    def get_info_exhibit(self, indx: int) -> str:
        return f'Описание экспоната {self.exhibits[indx].name}: {self.exhibits[indx].descr}'
