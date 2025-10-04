from . import CookingRecipe

from ..food import *

class Cake(CookingRecipe):
    xp = 100
    ingredients = [
        Egg,
        Flour,
        Milk
    ]
