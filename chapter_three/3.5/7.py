from typing import Tuple


class FileAcceptor:
    def __init__(self, *extensions: str):
        self.extensions = extensions

    def __call__(self, *args, **kwargs) -> bool:
        return '.' in args[0] and args[0].split('.')[-1] in self.extensions

    def __add__(self, other: 'FileAcceptor') -> 'FileAcceptor':
        return FileAcceptor(*set(self.extensions + other.extensions))


