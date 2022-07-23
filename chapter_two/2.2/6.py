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

    def push(self, obj: StackObj) -> None:
        if not self.top:
            self.top = obj
        else:
            iter_obj = self.top
            while iter_obj.next:
                iter_obj = iter_obj.next
            iter_obj.next = obj

    def pop(self) -> None:
        if not self.top:
            return
        if not self.top.next:
            self.top = None
        else:
            iter_obj = self.top
            while iter_obj.next:
                if iter_obj.next.next:
                    iter_obj = iter_obj.next
                else:
                    iter_obj.next = None
                    break

    def get_data(self) -> List[str]:
        result = []
        obj = self.top
        while obj:
            result.append(obj.data)
            obj = obj.next
        return result
