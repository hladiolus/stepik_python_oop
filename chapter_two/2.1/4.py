class Money:
    def __init__(self, money: int):
        self.__money = money

    def set_money(self, money: int) -> None:
        if self.__check_money(money):
            self.__money = money

    def get_money(self) -> int:
        return self.__money

    def add_money(self, mn: 'Money') -> None:
        self.__money += mn.__money

    def __check_money(self, money):
        return isinstance(money, int) and money >= 0
