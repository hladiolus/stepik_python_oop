TYPE_OS = 1  # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    def __new__(cls, *args, **kwargs):
        if TYPE_OS == 1:
            new_obj = DialogWindows()
        else:
            new_obj = DialogLinux()
        setattr(new_obj, 'name', args[0])
        return new_obj


dg = Dialog('test')
print(dg.name)
