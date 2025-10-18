from db import ItemModel

class Item:
    level = 1
    xp = 0

    def __init__(self, name, category=""):
        self.name = name
        self.category = category
        self._record, created = ItemModel.get_or_create(name=self.name, category=self.category)

    @property
    def cost(self):
        if hasattr(self, 'value'):
            return self.value
        return int( self.xp/10 )
