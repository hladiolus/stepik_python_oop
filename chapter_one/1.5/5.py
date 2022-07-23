from typing import Union


class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        if not all(map(lambda x: isinstance(x, (int, float)) and x > 0,
                       (self.a, self.b, self.c))):
            return 1

        if self.a + self.b <= self.c or \
                self.b + self.c <= self.a or \
                self.a + self.c <= self.b:
            return 2
        else:
            return 3


a, b, c = map(int, input().split()) # эту строчку не менять
tr = TriangleChecker(a, b, c)
print(tr.is_triangle())
