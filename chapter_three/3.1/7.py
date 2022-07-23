from typing import List


class App:
    __CREATED_APPS = {}
    __additional_var = None
    __name = ""

    def __new__(cls, *args, **kwargs):
        if cls not in cls.__CREATED_APPS:
            new_obj = object.__new__(cls)
            setattr(new_obj, 'name', cls.__name)
            if cls.__additional_var:
                setattr(new_obj, cls.__additional_var, args[0])
            cls.__CREATED_APPS[cls] = new_obj
        return cls.__CREATED_APPS[cls]


class AppVK(App):
    __name = "ВКонтакте"
    __additional_var = None


class AppYouTube(App):
    __name = "YouTube"
    __additional_var = "memory_max"


class AppPhone(App):
    __name = "Phone"
    __additional_var = "phone_list"


class SmartPhone:
    def __init__(self, model: str):
        self.model = model
        self.apps: List[App] = []

    def add_app(self, app: App) -> None:
        if isinstance(app, App) and app not in self.apps:
            self.apps.append(app)

    def remove_app(self, app) -> None:
        try:
            self.apps.remove(app)
        except ValueError:
            pass
        
