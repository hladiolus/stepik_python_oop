class Vector:
    def __init__(self, *coordinates):
        self.coordinates = list(coordinates)

    def __add__(self, other) -> 'Vector':
        slen = len(self.coordinates)
        if not slen == len(other.coordinates):
            raise ArithmeticError('размерности векторов не совпадают')
        return Vector(*[self.coordinates[i] + other.coordinates[i] for i in range(slen)])

    def __iadd__(self, other) -> 'Vector':
        slen = len(self.coordinates)
        if isinstance(other, int):
            for i in range(slen):
                self.coordinates[i] += other
        elif not slen == len(other.coordinates):
            raise ArithmeticError('размерности векторов не совпадают')
        else:
            for i in range(slen):
                self.coordinates[i] += other.coordinates[i]
        return self

    def __sub__(self, other) -> 'Vector':
        slen = len(self.coordinates)
        if not slen == len(other.coordinates):
            raise ArithmeticError('размерности векторов не совпадают')
        return Vector(*[self.coordinates[i] - other.coordinates[i] for i in range(slen)])

    def __isub__(self, other):
        slen = len(self.coordinates)
        if isinstance(other, int):
            for i in range(slen):
                self.coordinates[i] -= other
        elif not slen == len(other.coordinates):
            raise ArithmeticError('размерности векторов не совпадают')
        else:
            for i in range(slen):
                self.coordinates[i] -= other.coordinates[i]
        return self

    def __mul__(self, other) -> 'Vector':
        slen = len(self.coordinates)
        if not slen == len(other.coordinates):
            raise ArithmeticError('размерности векторов не совпадают')
        return Vector(*[self.coordinates[i] * other.coordinates[i] for i in range(slen)])

    def __imul__(self, other):
        slen = len(self.coordinates)
        if isinstance(other, int):
            for i in range(slen):
                self.coordinates[i] *= other
        elif not slen == len(other.coordinates):
            raise ArithmeticError('размерности векторов не совпадают')
        else:
            for i in range(slen):
                self.coordinates[i] *= other.coordinates[i]
        return self

    def __eq__(self, other: 'Vector') -> bool:
        if not len(self.coordinates) == len(other.coordinates):
            raise ArithmeticError('размерности векторов не совпадают')
        return self.coordinates == other.coordinates
