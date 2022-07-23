from typing import Tuple


class ImageFileAcceptor:
    def __init__(self, extensions: Tuple[str, ...]):
        self.extensions = extensions

    def __call__(self, *args, **kwargs):
        return '.' in args[0] and args[0].split('.')[1] in self.extensions
