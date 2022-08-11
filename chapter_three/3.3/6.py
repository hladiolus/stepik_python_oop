any_number = (int, float)


class Complex:
    def __init__(self, real: any_number, img: any_number):
        self.real = real
        self.img = img

    @property
    def real(self) -> any_number:
        return self.__real

    @real.setter
    def real(self, value: any_number) -> None:
        if isinstance(value, any_number):
            self.__real = value
        else:
            raise ValueError("Неверный тип данных.")

    @property
    def img(self) -> any_number:
        return self.__img

    @img.setter
    def img(self, value: any_number) -> None:
        if isinstance(value, any_number):
            self.__img = value
        else:
            raise ValueError("Неверный тип данных.")

    def __abs__(self):
        return (self.real**2 + self.img**2)**(1/2)


cmp = Complex(real=7, img=8)
cmp.real = 3
cmp.img = 4
c_abs = abs(cmp)
