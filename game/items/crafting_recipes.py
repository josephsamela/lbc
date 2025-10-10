from . import *

class CraftingRecipe(Item):
    def __init__(self, name, level, materials):
        self.name = name
        self.level = level
        self.xp = level*10
        self.materials = materials
        super().__init__(self.name)

# Materials
bead = Item('Bead')
feather = Item('Feather')
wire = Item('Wire')

# Lures
crankbait = CraftingRecipe('Crankbait', 1, [bead, feather, wire])

# Flies
pheasant_tail = CraftingRecipe('Pheasant Tail', 1, [bead, feather, wire])
