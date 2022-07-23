from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number: str) -> bool:
        splitted = number.split('-')
        return len(splitted) == 4 and all(map(lambda x: len(x) == 4 and x.isdigit(), splitted))

    @staticmethod
    def check_name(name: str) -> bool:
        if len(name.strip().split(' ')) != 2:
            return False

        return all(map(lambda x: x in CardCheck.CHARS_FOR_NAME, name.replace(' ')))
