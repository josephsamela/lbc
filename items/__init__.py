from db import *

import random

class ItemModel(Base):
    class Meta:
        db_table = 'items'
    name = CharField(unique=True)

class Item(Record):
    _model = ItemModel

class Bait(Item):
    pass

class Lure(Item):
    pass

class Fish(Item):
    def __init__(self):
        self.relative_size = self._relative_size()
        self.weight_lbs = self._weight()
        self.length_in = self._length()

    def _relative_size(self):
        # This property represents the "size" of the
        # fish relative to its maximum possible size.
        w = random.gauss(
            mu = 50,
            sigma = 13
        )
        if w > 100:
            return 100
        elif w < 5:
            return 5
        else:
            return w / 100

    def _weight(self):
        return self.relative_size * self.max_weight_lbs
        
    def _length(self):
        return self.relative_size * self.max_length_in
