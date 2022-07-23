class FloatValue:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if isinstance(value, float):
            return setattr(instance, self.name, value)
        else:
            raise TypeError("Присваивать можно только вещественный тип данных.")


class Cell:
    value = FloatValue()

    def __init__(self, value: float):
        self.value = value


class TableSheet:
    def __init__(self, n: int, m: int):
        self.cells = [[Cell(0.0) for _ in range(m)] for _ in range(n)]


table = TableSheet(5, 3)

counter = 1

for row in table.cells:
    for cell in row:
        cell.value = float(counter)
        counter += 1
