from db import ItemModel

class Item:
    level = 1
    xp = 0

    def __init__(self, name):
        self.name = name
        self._record, created = ItemModel.get_or_create(name=self.name)
