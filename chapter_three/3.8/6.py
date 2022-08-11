from typing import Optional, List


class StackObj:
    def __init__(self, data: str):
        self.__data: str = data
        self.__next: Optional['StackObj'] = None

    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, value: str) -> None:
        self.__data = value

    @property
    def next(self) -> 'StackObj':
        return self.__next

    @next.setter
    def next(self, value: 'StackObj') -> None:
        if value is None or isinstance(value, StackObj):
            self.__next = value


class Stack:
    def __init__(self):
        self.top: Optional[StackObj] = None
        self.__len = 0

    def push(self, obj: StackObj) -> None:
        if not self.top:
            self.top = obj
        else:
            iter_obj = self.top
            while iter_obj.next:
                iter_obj = iter_obj.next
            iter_obj.next = obj
        self.__len += 1

    def pop(self) -> None:
        if not self.top:
            return
        return_obj = None
        if not self.top.next:
            return_obj, self.top = self.top, None
        else:
            iter_obj = self.top
            while iter_obj.next:
                if iter_obj.next.next:
                    iter_obj = iter_obj.next
                else:
                    return_obj, iter_obj.next = iter_obj.next, None
                    break

        self.__len -= 1
        return return_obj

    def is_valid_index(self, idx: int) -> bool:
        return type(idx) == int and 0 <= idx < self.__len

    def __getitem__(self, item):
        if not self.is_valid_index(item):
            raise IndexError
        current_obj = self.top
        while item:
            current_obj = current_obj.next
            item -= 1
        return current_obj

    def __setitem__(self, key, value):
        if not self.is_valid_index(key):
            raise IndexError
        if not isinstance(value, StackObj):
            raise ValueError
        if key == 0:
            if self.top:
                value.next = self.top.next
            self.top = value
        else:
            key -= 1
            current_obj = self.top
            while key:
                current_obj = current_obj.next
                key -= 1
            if current_obj.next:
                value.next = current_obj.next.next
            current_obj.next = value
