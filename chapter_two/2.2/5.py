class WindowDlg:
    def __init__(self, title: str, width: int, height: int):
        self.__title: str = title
        self.__width: int = width
        self.__height: int = height

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, value: str) -> None:
        self.__title = value

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, value: int) -> None:
        if isinstance(value, int) and 0 <= value <= 10000:
            self.__width = value
            self.show()

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, value: int) -> None:
        if isinstance(value, int) and 0 <= value <= 10000:
            self.__height = value
            self.show()

    def show(self):
        print(f'{self.title}: {self.width}, {self.height}')
