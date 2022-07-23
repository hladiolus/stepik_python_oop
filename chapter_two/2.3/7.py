from typing import List


class ValidateString:
    def __init__(self, min_length: int, max_length: int):
        self.__min_length = min_length
        self.__max_length = max_length

    def validate(self, string: str) -> bool:
        return isinstance(string, str) and \
               self.__min_length <= len(string) <= self.__max_length


class StringValue:
    def __init__(self, validator: ValidateString):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validator.validate(value):
            return setattr(instance, self.name, value)


class RegisterForm:
    login = StringValue(validator=ValidateString(3, 100))
    password = StringValue(validator=ValidateString(3, 100))
    email = StringValue(validator=ValidateString(3, 100))

    def __init__(self, login: str, password: str, email: str):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self) -> List[str]:
        return [self.login, self.password, self.email]

    def show(self):
        print(f"""<form>
Логин: {self.login}
Пароль: {self.password}
Email: {self.email}
</form>""")
