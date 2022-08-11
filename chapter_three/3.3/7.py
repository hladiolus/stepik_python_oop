from typing import List, Tuple, Union

any_number = (int, float)


class RadiusVector:
    def __init__(self, *args):
        if len(args) == 1:
            self.vec: List[any_number] = [0 for i in range(args[0])]
            self._len = args[0]
        else:
            self.vec: List[any_number] = list(args)
            self._len = len(args)

    def set_coords(self, *coordinates) -> None:
        for idx in range(min(len(coordinates), self._len)):
            self.vec[idx] = coordinates[idx]

    def get_coords(self):
        return tuple(self.vec)

    def __len__(self) -> int:
        return self._len

    def __abs__(self) -> float:
        return sum([i*i for i in self.vec])**(1/2)
