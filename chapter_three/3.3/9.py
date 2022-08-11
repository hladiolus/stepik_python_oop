from typing import List, Tuple


class Ingredient:
    def __init__(self, name: str, volume: float, measure: str):
        self.name = name
        self.volume = volume
        self.measure = measure

    def __str__(self):
        return f'{self.name}: {self.volume}, {self.measure}'


class Recipe:
    def __init__(self, *ingredients):
        self.ingredients: List[Ingredient] = list(ingredients)

    def add_ingredient(self, ing: Ingredient) -> None:
        if isinstance(ing, Ingredient):
            self.ingredients.append(ing)

    def remove_ingredient(self, ing: Ingredient):
        try:
            self.ingredients.remove(ing)
        except ValueError:
            pass

    def get_ingredients(self) -> Tuple[Ingredient, ...]:
        return tuple(self.ingredients)

    def __len__(self):
        return len(self.ingredients)
