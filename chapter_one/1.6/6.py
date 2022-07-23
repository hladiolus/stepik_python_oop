class AbstractClass:
    def __new__(self, *args, **kwargs):
        return "Ошибка: нельзя создавать объекты абстрактного класса"
