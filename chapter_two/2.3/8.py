class StringValue:
    def __init__(self, min_length: int, max_length: int):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if isinstance(value, str) and self.min_length <= len(value) <= self.max_length:
            return setattr(instance, self.name, value)


class PriceValue:
    def __init__(self, max_value: float | int):
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value: float | int):
        if isinstance(value, (float, int)) and 0 <= value <= self.max_value:
            return setattr(instance, self.name, value)


class Product:
    name = StringValue(2, 50)
    price = PriceValue(10000)

    def __init__(self, name: str, price: float | int):
        self.name = name
        self.price = price


class SuperShop:
    def __init__(self, name: str):
        self.name = name
        self.goods = []

    def add_product(self, product: Product) -> None:
        self.goods.append(product)

    def remove_product(self, product: Product) -> None:
        self.goods.remove(product)
