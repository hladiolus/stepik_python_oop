from typing import Union, Tuple


class Ellipse:
    def __new__(cls, *args, **kwargs):
        if len(args) > 4:
            raise ValueError
        obj = super().__new__(cls)
        attrs = ('x1', 'y1', 'x2', 'y2')
        for idx, arg in enumerate(args):
            if type(arg) not in (int, float):
                raise ValueError
            setattr(obj, attrs[idx], arg)
        return obj

    def get_coords(self) -> Tuple[Union[int, float]]:
        if not self:
            raise AttributeError('нет координат для извлечения')
        return self.x1, self.y1, self.x2, self.y2

    def __bool__(self):
        return hasattr(self, 'y2')


lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(1, 2, 3, 4)]
for i in lst_geom:
    if i:
        i.get_coords()
