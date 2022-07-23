class Application:
    def __init__(self, name: str, blocked: bool = False):
        self.name = name
        self.blocked = blocked


class AppStore:
    def __init__(self):
        self.store = []

    def add_application(self, app: Application) -> None:
        self.store.append(app)

    def remove_application(self, app) -> None:
        self.store.remove(app)

    def block_application(self, app) -> None:
        app.blocked = True

    def total_apps(self) -> int:
        return len(self.store)