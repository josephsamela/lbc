from game.items import Item

class Food(Item):

    cookable = False

    def __init__(self):
        # Food is raw by default. But contains a cooked version of itself.
        if self.cookable:
            self.state = 'Raw'
            c = self.__class__
            n = c.__name__
            self.cooked = type(n, (c,), {'state': 'Cooked', 'cookable': False})

    @property
    def name(self):
        n = super().name

        if not self.state:
            return n
        return f'{self.state} {n}'

from .baking import *
