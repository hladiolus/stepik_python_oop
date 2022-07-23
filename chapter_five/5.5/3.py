class PrimaryKey:
    def __enter__(self):
        print('вход')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        return exc_type


with PrimaryKey() as pk:
    raise ValueError