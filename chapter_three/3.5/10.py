from typing import Union, List


class Thing:
    def __init__(self, name: str, mass: Union[int, float]):
        self.name = name
        self.mass = mass

    def __eq__(self, other: 'Thing'):
        if isinstance(other, Thing):
            return self.name.lower() == other.name.lower() and self.mass == other.mass
        else:
            raise ValueError


class Box:
    def __init__(self):
        self.things: List[Thing] = []

    def add_thing(self, obj: Thing):
        if isinstance(obj, Thing):
            self.things.append(obj)

    def get_things(self) -> List[Thing]:
        return self.things

    def __eq__(self, other: 'Box'):
        if isinstance(other, Box):
            if len(self.things) == len(other.things):
                copy = other.things[:]
                for thing1 in self.things:
                    for idx, thing2 in enumerate(copy):
                        if thing1 == thing2:
                            copy.pop(idx)
                            break
                    else:
                        return False
                return True
            else:
                return False
