class Translator:
    def __init__(self):
        self._translates = {}

    def add(self, eng, rus):
        self._translates[eng] = self._translates.get(eng, []) + [rus]

    def remove(self, eng):
        self._translates.pop(eng)

    def translate(self, eng):
        return self._translates.get(eng, [])


tr = Translator()
tr.add('tree', 'дерево')
tr.add('car', 'машина')
tr.add('car', 'автомобиль')
tr.add('leaf', 'лист')
tr.add('river', 'река')
tr.add('go', 'идти')
tr.add('go', 'ехать')
tr.add('go', 'ходить')
tr.add('milk', 'молоко')
tr.remove('car')
print(*tr.translate('go'))
