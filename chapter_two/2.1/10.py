from string import ascii_uppercase, ascii_lowercase, digits
from random import choices


class EmailValidator:
    __ALPH = ascii_uppercase + ascii_lowercase + digits + '_.'

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def check_email(cls, email: str) -> bool:

        if email.count('@') != 1 or '..' in email or not cls.__is_email(email):
            return False

        l, r = email.split('@')
        if len(l) > 100 or len(r) > 50 or '.' not in r:
            return False

        if any(map(lambda x: x not in cls.__ALPH + '@', email)):
            return False
        return True
    
    @classmethod
    def get_random_email(cls) -> str:
        return ''.join(choices(cls.__ALPH, k=10)) + '@gmail.com'

    @staticmethod
    def __is_email_str(email: str) -> bool:
        return isinstance(email, str)