class Book:
    __VAR_TYPES = {
        'title': str,
        'author': str,
        'pages': int,
        'year': int
    }

    def __init__(self, title: str = '', author: str = '', pages: int = 0, year: int = 0):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value):
        if key in self.__VAR_TYPES:
            if isinstance(value, self.__VAR_TYPES[key]):
                object.__setattr__(self, key, value)
            else:
                raise TypeError("Неверный тип присваиваемых данных.")
        else:
            object.__setattr__(self, key, value)


book = Book('Python ООП', 'Сергей Балакирев', 123, 2022)
