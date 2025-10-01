from game.skills import Skill
from .recipes import CraftingRecipes

class Crafting(Skill):
    name = 'Crafting'
    recipes = CraftingRecipes()
