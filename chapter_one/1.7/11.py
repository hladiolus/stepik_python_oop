from typing import List


class Message:
    def __init__(self, text: str, fl_like: bool = False):
        self.text = text
        self.fl_like = fl_like


class Viber:
    _messages = []

    @staticmethod
    def add_message(msg: Message) -> None:
        Viber._messages.append(msg)

    @staticmethod
    def remove_message(msg: Message) -> None:
        Viber._messages.remove(msg)

    @staticmethod
    def set_like(msg: Message):
        msg.fl_like = bool((msg.fl_like - 1) ** 2)

    @staticmethod
    def show_last_message(count: int) -> List[Message]:
        return Viber._messages[:-count]

    @staticmethod
    def total_messages() -> int:
        return len(Viber._messages)
