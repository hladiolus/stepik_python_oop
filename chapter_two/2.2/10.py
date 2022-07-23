from typing import List


class PhoneNumber:
    def __init__(self, number: int, fio: str):
        if isinstance(number, int) and len(str(number)) == 11:
            self.number = number
        else:
            raise ValueError()

        if isinstance(fio, str):
            self.fio = fio
        else:
            raise ValueError()


class PhoneBook:
    def __init__(self):
        self.__phone_numbers_list = []

    def add_phone(self, phone: PhoneNumber) -> None:
        self.__phone_numbers_list.append(phone)

    def remove_phone(self, indx: int) -> None:
        self.__phone_numbers_list.pop(indx)

    def get_phone_list(self) -> List[PhoneNumber]:
        return self.__phone_numbers_list
