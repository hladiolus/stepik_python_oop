from random import randint


class Cell:
    def __init__(self, around_mines, mine):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = True


class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = [[Cell(0, False) for _ in range(N)][:] for _ in range(N)]

    def init(self):
        left_mines = self.M
        while left_mines:
            row = randint(0, self.N - 1)
            col = randint(0, self.N - 1)
            if self.pole[row][col].mine:
                continue
            self.pole[row][col].mine = True
            self.update_square(row, col)
            left_mines -= 1

    def update_square(self, row, col):
        for r in range(max(row - 1, 0), min(row + 2, self.N)):
            for c in range(max(col - 1, 0), min(col + 2, self.N)):
                cell = self.pole[r][c]
                if cell.mine:
                    cell.around_mines = 0
                else:
                    cell.around_mines += 1

    def show(self):
        print('\n'.join([''.join([str(i.around_mines) if i.fl_open else '#' for i in row]) for row in self.pole]))


gp = GamePole(10, 12)
gp.init()

print(gp.show())
