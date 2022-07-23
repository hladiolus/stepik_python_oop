from typing import Tuple


class Line:
    def __init__(self, x1: int, y1: int, x2: int, y2: int):
        self.__x1 = self.__x2 = self.__y1 = self.__y2 = None
        self.set_coords(x1, y1, x2, y2)

    def set_coords(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

    def get_coords(self) -> Tuple[int, int, int, int]:
        return self.__x1, self.__y1, self.__x2, self.__y2

    def draw(self) -> None:
        print(*self.get_coords())
