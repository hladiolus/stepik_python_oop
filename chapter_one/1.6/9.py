class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def clone(self):
        new_obj = super().__new__(Point)
        for k, v in self.__dict__.items():
            setattr(new_obj, k, v)
        return new_obj

