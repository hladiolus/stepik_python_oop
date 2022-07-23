from typing import Optional


class ObjList:
    def __init__(self, data: str):
        self.__next: Optional['ObjList'] = None
        self.__prev: Optional['ObjList'] = None
        self.__data: Optional[str] = data

    def set_next(self, obj: Optional['ObjList']) -> None:
        self.__next = obj

    def set_prev(self, obj: Optional['ObjList']) -> None:
        self.__prev = obj

    def get_next(self) -> Optional['ObjList']:
        return self.__next

    def get_prev(self) -> Optional['ObjList']:
        return self.__prev

    def set_data(self, data: Optional[str]) -> None:
        self.__data = data

    def get_data(self) -> Optional[str]:
        return self.__data


class LinkedList:
    def __init__(self):
        self.head: Optional[ObjList] = None
        self.tail: Optional[ObjList] = None

    def add_obj(self, obj: ObjList) -> None:
        self.head = self.head or obj
        if self.tail:
            self.tail.set_next(obj)

        obj.set_prev(self.tail)

        self.tail = obj

    def remove_obj(self) -> None:
        prev = self.tail.get_prev()

        if not prev:
            self.tail = None
            self.head = None
        else:
            prev.set_next(None)
            self.tail.set_prev(None)
            self.tail = prev

    def get_data(self):
        result = []
        current_obj = self.head
        while current_obj:
            result.append(current_obj.get_data())
            current_obj = current_obj.get_next()
        return result

lst = LinkedList()
lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
res = lst.get_data()    # ['данные 1', 'данные 2', 'данные 3']
print(res)