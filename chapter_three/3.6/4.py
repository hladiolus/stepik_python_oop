    from typing import TypeVar

    T = TypeVar("T", int, float)


    class Rect:
        def __init__(self, x: T, y: T, width: T, height: T):
            self.x = x
            self.y = y
            self.width = width
            self.height = height

        def __hash__(self):
            return hash((self.width, self.height))

