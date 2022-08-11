from typing import Optional


class StackObj:
    def __init__(self, data: str):
        self.__data = data
        self.next: Optional['StackObj'] = None

    @property
    def next(self) -> Optional['StackObj']:
        return self.__next

    @next.setter
    def next(self, value: Optional['StackObj']) -> None:
        self.__next = value

    def __repr__(self):
        return self.__data


class Stack:
    def __init__(self):
        self.top: Optional[StackObj] = None

    def push_back(self, obj: StackObj) -> None:
        if self.top:
            curr_obj = self.top
            while curr_obj.next:
                curr_obj = curr_obj.next
            curr_obj.next = obj
        else:
            self.top = obj

    def pop_back(self):
        if self.top:
            if self.top.next:
                curr_obj = self.top
                while curr_obj.next.next:
                    curr_obj = curr_obj.next
                curr_obj.next = None
            else:
                self.top = None
        else:
            raise IndexError

    def __add__(self, other):
        if isinstance(other, StackObj):
            self.push_back(other)
        return self

    def __mul__(self, other):
        if isinstance(other, (list, tuple)):
            for elem in other:
                if isinstance(elem, str):
                    self.push_back(StackObj(elem))
        return self
