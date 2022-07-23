from random import randint as ri
from random import choice


class Figure:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


class Line(Figure):
    pass


class Rect(Figure):
    pass


class Ellipse(Figure):
    pass


elements = [choice((Line, Rect, Ellipse))(*[ri(1, 100) for _ in range(4)])]
for i in elements:
    if isinstance(i, Line):
        i.sp = (0, 0)
        i.ep = (0, 0)
