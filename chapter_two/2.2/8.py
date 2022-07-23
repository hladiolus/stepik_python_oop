from typing import Optional, List


class TreeObj:
    def __init__(self, indx: int, value: Optional[str] = None):
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self) -> Optional['TreeObj']:
        return self.__left

    @left.setter
    def left(self, value: Optional['TreeObj']) -> None:
        self.__left = value

    @property
    def right(self) -> Optional['TreeObj']:
        return self.__right

    @right.setter
    def right(self, value: Optional['TreeObj']) -> None:
        self.__right = value

    def get_next_by_num(self, num: int) -> 'TreeObj':
        if num == 1:
            return self.left
        elif num == 0:
            return self.right


class DecisionTree:
    @classmethod
    def predict(cls, root: TreeObj, x: List[int]):
        current_obj = root
        while True:
            if current_obj.value is not None:
                return current_obj.value
            if not current_obj.left and not current_obj.right:
                return None
            current_obj = current_obj.get_next_by_num(x[current_obj.indx])

    @classmethod
    def add_obj(cls, obj: TreeObj, node: TreeObj = None, left: bool = True):
        if node:
            if left:
                node.left = obj
            else:
                node.right = obj
        return obj
