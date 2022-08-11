from typing import Dict, Any


class Model:
    def __init__(self):
        self.fields: Dict[str, Any] = {}

    def query(self, **fields) -> None:
        self.fields.update(fields)

    def __str__(self) -> str:
        return f'Model' \
               f'{": "*(len(self.fields) > 0)}' \
               f'{", ".join([f"{k} = {v}" for k, v in self.fields.items()])}'
