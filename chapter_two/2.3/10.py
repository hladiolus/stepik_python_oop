from typing import List


class Telecast:
    def __init__(self, id: int, name: str, duration: int):
        self.__id = id
        self.__name = name
        self.__duration = duration

    @property
    def uid(self) -> int:
        return self.__id

    @uid.setter
    def uid(self, value: int) -> None:
        self.__id = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, value: int) -> None:
        self.__duration = value


class TVProgram:
    def __init__(self, channel_name: str):
        self.channel_name = channel_name
        self.items: List[Telecast] = []

    def add_telecast(self, tl: Telecast) -> None:
        self.items.append(tl)

    def remove_telecast(self, indx: int) -> None:
            for item in self.items:
                if item.uid == indx:
                    self.items.remove(item)
                    break
