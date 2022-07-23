class Good:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Table(Good):
    pass


class TV(Good):
    pass


class Notebook(Good):
    pass


class Cup(Good):
    pass


class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f'{i.name}: {i.price}' for i in self.goods]


cart = Cart()

cart.add(TV('tv1', 1000))
cart.add(TV('tv2', 1000))
cart.add(Table('table', 2000))
cart.add(Notebook('nb1', 3000))
cart.add(Notebook('nb2', 3000))
cart.add(Cup('cup', 50))
