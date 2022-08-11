from typing import Tuple


class TimeVar:
    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, instance, owner) -> int:
        return getattr(instance, self.name)

    def __set__(self, instance, value) -> None:
        if isinstance(value, int) and value >= 0:
            setattr(instance, self.name, value)


class Clock:
    hours = TimeVar()
    minutes = TimeVar()
    seconds = TimeVar()

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __sub__(self, other):
        return self.get_time() - other.get_time()

    def get_time(self) -> int:
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @staticmethod
    def from_seconds(seconds: int) -> Tuple[int, int, int]:
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = (seconds % 3600) % 60
        return hours, minutes, seconds


class DeltaClock:
    def __init__(self, clock1: Clock, clock2: Clock):
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self):
        diff = self.clock1 - self.clock2
        return ': '.join(map(lambda x: f'{x:02d}', Clock.from_seconds(diff if diff > 0 else 0)))

    def __len__(self):
        return self.clock1 - self.clock2

    def __repr__(self):
        return self.__str__()


cl = DeltaClock(Clock(1, 2, 3), Clock(3, 4, 5))
print(cl)