import sys


class Player:
    def __init__(self, name: str, old: int, score: int):
        if type(old) != int or type(score) != int or type(name) != str:
            raise ValueError

        self.name = name
        self.old = old
        self.score = score

    def __bool__(self):
        return self.score > 0


lst_in = list(map(str.strip, sys.stdin.readlines()))
players = []

for line in lst_in:
    name, old, score = line.split('; ')
    players.append(Player(name, int(old), int(score)))

players_filtered = list(filter(bool, players))
