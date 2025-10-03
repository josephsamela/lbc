from . import CookingRecipe

from ..food import *

class Cake(CookingRecipe):
    required_level = 1
    xp = 100
    ingredients = [
        Egg,
        Flour,
        Milk
    ]
