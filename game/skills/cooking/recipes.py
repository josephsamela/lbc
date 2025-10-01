import random

class CookingRecipe:
    def __init__(self):
        pass

class CookedSalmon(CookingRecipe):
    name = 'Cooked Salmon'

class CookedCarrots(CookingRecipe):
    name = 'Cooked Carrots'

class CookingRecipes:
    cooked_salmon = CookedSalmon
    cooked_carrots = CookedCarrots
