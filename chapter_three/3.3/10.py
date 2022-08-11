from typing import Tuple, List


class PolyLine:
    def __init__(self, *points):
        self.points: List[Tuple[int, int]] = list(points)

    def add_coord(self, x: int, y: int) -> None:
        if isinstance(x, int) and isinstance(y, int):
            self.points.append((x, y))

    def remove_coord(self, indx: int) -> None:
        try:
            self.points.pop(indx)
        except IndexError:
            pass

    def get_coords(self) -> Tuple[Tuple[int, int], ...]:
        return tuple(self.points)
