from typing import List


class LessonItem:
    def __init__(self, title: str, practices: int, duration: int):
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if key in ["practices", "duration"]:
            if not isinstance(value, int) or value < 0:
                raise TypeError("Неверный тип присваиваемых данных.")
        elif key == "title" and not isinstance(value, str):
            raise TypeError("Неверный тип присваиваемых данных.")
        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if item not in ['title', 'practices', 'duration']:
            object.__delattr__(self, item)


class Module:
    def __init__(self, name: str):
        self.name = name
        self.lessons: List[LessonItem] = []

    def add_lesson(self, lesson: LessonItem) -> None:
        if isinstance(lesson, LessonItem):
            self.lessons.append(lesson)

    def remove_lesson(self, indx: int) -> None:
        self.lessons.pop(indx)


class Course:
    def __init__(self, name: str):
        self.name = name
        self.modules: List[Module] = []

    def add_module(self, module: Module) -> None:
        if isinstance(module, Module):
            self.modules.append(module)

    def remove_module(self, indx: int) -> None:
        self.modules.pop(indx)

