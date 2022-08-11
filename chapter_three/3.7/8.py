from typing import List
from random import randint


class Cell:
    def __init__(self):
        self.is_mine = False
        self.number = 0
        self.is_open = True

    def __bool__(self):
        return not self.is_open

    @property
    def is_mine(self) -> bool:
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, value: bool) -> None:
        if type(value) != bool:
            raise ValueError("недопустимое значение атрибута")

        self.__is_mine = value

    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, value: int) -> None:
        if type(value) != int or value < 0 or value > 8:
            raise ValueError("недопустимое значение атрибута")
        self.__number = value

    @property
    def is_open(self) -> bool:
        return self.__is_open

    @is_open.setter
    def is_open(self, value: bool) -> None:
        if type(value) != bool:
            raise ValueError("недопустимое значение атрибута")
        self.__is_open = value

    def __str__(self):
        return '■' if not self.is_open else 'M' if self.is_mine else str(self.number)


class GamePole:
    __instance = None

    def __new__(cls, *args, **kwargs):
        GamePole.__instance = GamePole.__instance or super().__new__(cls)
        return GamePole.__instance

    def __init__(self, N: int, M: int, total_mines: int):
        self.N = N
        self.M = M
        self.total_mines = total_mines
        self.__pole_cells: List[List[Cell]] = [[Cell() for i in range(M)] for j in range(N)]

    @property
    def pole(self) -> List[List[Cell]]:
        return self.__pole_cells

    def init_pole(self) -> None:
        mines_left = self.total_mines
        while mines_left:
            x, y = randint(0, self.N - 1), randint(0, self.M - 1)
            if self.__pole_cells[x][y].is_mine:
                continue
            self.__pole_cells[x][y].is_mine = True
            self.update_square(x, y)
            mines_left -= 1

        for row in self.__pole_cells:
            for cell in row:
                cell.is_open = False

    def update_square(self, x: int, y: int) -> None:
        for _x in range(max(x - 1, 0), min(x + 2, self.N)):
            for _y in range(max(y - 1, 0), min(y + 2, self.M)):
                if not self.__pole_cells[_x][_y].is_mine:
                    self.__pole_cells[_x][_y].number += 1

    def open_cell(self, i: int, j: int):
        if type(i) != int or type(j) != int or i >= self.N or j >= self.M:
            raise IndexError('некорректные индексы i, j клетки игрового поля')

        self.__pole_cells[i][j].is_open = True

    def show_pole(self) -> None:
        print('\n'.join([''.join([str(i) for i in row]) for row in self.__pole_cells]))
