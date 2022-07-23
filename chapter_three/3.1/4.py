from typing import Union


class Product:
    __UNIQUE_ID = 1
    __VAR_TYPES = {
        'name': str,
        'weight': (int, float),
        'price': (int, float)
    }

    def __new__(cls, *args, **kwargs):
        new_obj = super().__new__(cls)
        setattr(new_obj, 'id', cls.__UNIQUE_ID)
        cls.__UNIQUE_ID += 1
        return new_obj

    def __init__(self, name: str, weight: Union[int, float], price: Union[int, float]):
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if key == 'weight' or key == 'price':
            if not isinstance(value, (float, int)) or value < 0:
                raise TypeError("Неверный тип присваиваемых данных.")
        elif key == 'name' and not isinstance(value, str):
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")


class Shop:
    def __init__(self, name: str):
        self.name = name
        self.goods = []

    def add_product(self, product: Product) -> None:
        self.goods.append(product)

    def remove_product(self, product: Product) -> None:
        self.goods.remove(product)

