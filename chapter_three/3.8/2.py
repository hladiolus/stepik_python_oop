class Record:
    def __init__(self, **fields):
        for k, v in fields.items():
            setattr(self, k, v)

    def __setitem__(self, key, value):
        if not isinstance(key, int) and key >= len(self.__dict__):
            raise IndexError

        self.__dict__[tuple(self.__dict__.keys())[key]] = value

    def __getitem__(self, item):
        if not isinstance(item, int) and item >= len(self.__dict__):
            raise IndexError

        return self.__dict__[tuple(self.__dict__.keys())[item]]
