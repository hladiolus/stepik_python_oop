from typing import Optional


class ObjList:
    def __init__(self, data: str):
        self.data = data
        self.prev = None
        self.next = None

    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, value: str) -> None:
        self.__data = value

    @property
    def prev(self) -> Optional['ObjList']:
        return self.__prev

    @prev.setter
    def prev(self, value: Optional['ObjList']) -> None:
        self.__prev = value

    @property
    def next(self) -> Optional['ObjList']:
        return self.__next

    @next.setter
    def next(self, value: Optional['ObjList']) -> None:
        self.__next = value


class LinkedList:
    def __init__(self):
        self.head: Optional[ObjList] = None
        self.tail: Optional[ObjList] = None
        self._len = 0

    def add_obj(self, obj: ObjList) -> None:
        if not self.tail:
            self.head = obj
        else:
            self.tail.next = obj
            obj.prev = self.tail

        self.tail = obj
        self._len += 1

    def remove_obj(self, indx: int) -> None:
        if not self._len:
            raise IndexError
        if indx == 0:
            self.head = self.head.next
        elif indx == self._len - 1:
            self.tail = self.tail.prev
        else:
            obj = self.get_object_by_index(indx)
            obj.prev = obj.next
        self._len -= 1

    def get_object_by_index(self, indx: int) -> Optional[ObjList]:
        if self._len // 2 <= indx:
            indx = self._len - indx - 1
            curr_obj = self.tail
            while indx:
                curr_obj = curr_obj.prev
                indx -= 1
        else:
            curr_obj = self.head
            while indx:
                curr_obj = curr_obj.next
                indx -= 1
        return curr_obj

    def __len__(self) -> int:
        return self._len

    def __call__(self, *args, **kwargs) -> str:
        return self.get_object_by_index(args[0]).data
