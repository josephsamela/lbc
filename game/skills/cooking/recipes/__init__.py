from game.skills.cooking.food import Food

class CookingRecipe(Food):
    ingredients = []
    required_level = 0
    xp = 0
    states = ['Cooked', 'Burnt']

    @property
    def name(self):
        n = super().name
        match self.state:
            case 'Cooked':
                return n
            case _:
                return f'{self.state} {n}'

from .desserts import *
