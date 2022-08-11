from typing import List, TypeVar, Optional

T = TypeVar("T")


class NewList:
    def __init__(self, lst: Optional[List[T]] = None):
        if lst is None:
            lst = []
        self.lst: List[T] = lst

    def get_list(self) -> List[T]:
        return self.lst

    @staticmethod
    def remove_similar(lst1: List[T], lst2: List[T]) -> List[T]:
        lst1 = lst1[:]
        for elem2 in lst2:
            for j, elem1 in enumerate(lst1):
                if elem2 == elem1 and type(elem2) == type(elem1):
                    del lst1[j]
                    break
        return lst1

    def __sub__(self, other):
        if isinstance(other, NewList):
            other = other.lst
        if not isinstance(other, list):
            raise ValueError
        return NewList(self.remove_similar(self.lst, other))

    def __rsub__(self, other):
        return NewList(other).__sub__(self)
