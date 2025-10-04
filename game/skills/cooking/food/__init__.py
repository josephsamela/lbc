from game.items import Item

class Food(Item):
    required_level = 0
    xp = 0

    @property
    def cookable(self):
        match self.state:
            case 'Raw': 
                return True
            case _:
                return False

class CookableFood(Food):
    states = ['Raw', 'Cooked', 'Burnt']
    @property
    def name(self):
        n = super().name
        return f'{self.state} {n}'

from .baking import *
