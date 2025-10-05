from game.items import Item

class CraftingRecipe(Item):
    materials = []
    required_level = 0

    @property
    def xp(self):
        return self.required_level*10
