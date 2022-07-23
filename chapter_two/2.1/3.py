class Clock:
    def __init__(self, time: int = 0):
        self.__time = time

    def set_time(self, tm: int) -> None:
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self) -> int:
        return self.__time

    def __check_time(self, tm):
        return isinstance(tm, int) and 0 <= tm < 100000


clock = Clock()
clock.set_time(4530)