import random

class CraftingRecipe:
    def __init__(self):
        pass

class Crankbait(CraftingRecipe):
    name = 'Trowel'

class Spinner(CraftingRecipe):
    name = 'Spinner'

class Popper(CraftingRecipe):
    name = 'Popper'

class CraftingRecipes:
    crankbait = Crankbait
    spinner = Spinner
    popper = Popper
