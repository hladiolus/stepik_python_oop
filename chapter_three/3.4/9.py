any_num = (int, float)


class Box3D:
    def __init__(self, width: any_num, height: any_num, depth: any_num):
        self.width = width
        self.height = height
        self.depth = depth

    def __add__(self, other: 'Box3D') -> 'Box3D':
        return Box3D(self.width + other.width, self.height + other.height, self.depth + other.depth)

    def __sub__(self, other: 'Box3D') -> 'Box3D':
        return Box3D(self.width - other.width, self.height - other.height, self.depth - other.depth)

    def __mul__(self, other):
        return Box3D(self.width * other, self.height * other, self.depth * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __floordiv__(self, other):
        return Box3D(self.width // other, self.height // other, self.depth // other)

    def __mod__(self, other):
        return Box3D(self.width % other, self.height % other, self.depth % other)
