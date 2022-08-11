from typing import Tuple, List, Type


class IntegerValue:
    def __set_name__(self, owner, name):
        self._name = "__" + name

    def __set__(self, instance, value):
        if type(value) != int:
            raise ValueError

        setattr(instance, self._name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self._name)


class CellInteger:
    value = IntegerValue()

    def __init__(self, start_value: int):
        self.value = start_value


class TableValues:
    def __init__(self, rows, cols, cell: Type[CellInteger] = None):
        if not cell:
            raise ValueError

        self.cells: Tuple[Tuple[CellInteger, ...]] = tuple([tuple([cell(0) for i in range(cols)]) for _ in range(rows)])

    def __getitem__(self, item):
        return self.cells[item[0]][item[1]].value

    def __setitem__(self, key, value):
        self.cells[key[0]][key[1]].value = value


table = TableValues(2, 3, cell=CellInteger)
print(table[0, 1])
table[1, 1] = 10
# table[0, 0] = 1.45 # генерируется исключение ValueError

# вывод таблицы в консоль
for row in table.cells:
    for x in row:
        print(x.value, end=' ')
    print()