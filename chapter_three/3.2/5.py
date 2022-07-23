class DigitRetrieve:
    def __call__(self, *args, **kwargs):
        try:
            return int(args[0])
        except ValueError:
            return None
