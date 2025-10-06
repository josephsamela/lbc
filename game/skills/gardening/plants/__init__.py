from game.items import Item

class Plant(Item):

    states = ['Seed', 'Fruit']

    @property
    def name(self):
        n = super().name
        if self.state == 'Seed':    
            return f'{n} {self.state}'
        return n

from .vegetables import *
