from typing import Union, Optional
from functools import total_ordering


class CentralBank:
    rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def register(cls, money: 'Money') -> None:
        money.cb = cls


@total_ordering
class Money:
    __name: str

    def __init__(self, volume: Union[int, float]):
        self.volume = float(volume)
        self.cb: Optional[CentralBank] = None

    @property
    def volume(self) -> float:
        return self._volume

    @volume.setter
    def volume(self, value: float) -> None:
        self._volume = value

    @property
    def cb(self) -> Optional[CentralBank]:
        return self._cb

    @cb.setter
    def cb(self, value: Optional[CentralBank]) -> None:
        self._cb = value

    def get_money_in_dollars(self) -> float:
        if self.cb:
            return self.volume / self.cb.rates[self.__name__]
        else:
            raise ValueError("Неизвестен курс валют.")

    def __eq__(self, other: 'Money'):
        return other.get_money_in_dollars() / 1.1 <= self.get_money_in_dollars() <= other.get_money_in_dollars() * 1.1

    def __lt__(self, other: 'Money'):
        return self.get_money_in_dollars() < other.get_money_in_dollars()


class MoneyR(Money):
    __name__ = 'rub'


class MoneyD(Money):
    __name__ = 'dollar'


class MoneyE(Money):
    __name__ = 'euro'
