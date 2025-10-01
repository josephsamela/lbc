from game.skills import Skill
from .recipes import CookingRecipe

class Cooking(Skill):
    name = 'Cooking'
    recipes = CookingRecipe()
