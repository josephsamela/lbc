from . import *

from .fish import fish

class CookingRecipe(Item):
    def __init__(self, name_success, name_failure, level, ingredients, xp_bonus=10, category="food"):
        self.name = name_success
        self.level = level
        self.xp = level*xp_bonus
        self.ingredients = ingredients
        self.burnt = Item(name_failure, 'burnt food')
        self.category = category
        super().__init__(self.name, self.category)

# Ingredients
flour = Item('Flour', 'ingredient')
egg = Item('Egg', 'ingredient')
milk = Item('Milk', 'ingredient')

cooking_recipes = {
    'skill': 'cooking',
    'deserts': {
        'cake': CookingRecipe('Cake', 'Burnt Cake', 1, [flour, egg, milk], xp_bonus=100)
    },
    'fish': {
        'cooked_scup': CookingRecipe('Cooked Scup', 'Burnt Scup', 1, [fish['ocean']['raw_scup']])
        # 'cooked_pink_salmon': CookingRecipe('Cooked Pink Salmon', 'Burnt Pink Salmon', 1, [fish['raw_pink_salmon']]),
        # 'cooked_coho_salmon': CookingRecipe('Cooked Coho Salmon', 'Burnt Coho Salmon', 1, [fish['raw_coho_salmon']]),
        # 'cooked_sockeye_salmon': CookingRecipe('Cooked Sockeye Salmon', 'Burnt Sockeye Salmon', 1, [fish['raw_sockeye_salmon']]),
        # 'cooked_chinook_salmon': CookingRecipe('Cooked Chinook Salmon', 'Burnt Chinook Salmon', 1, [fish['raw_chinook_salmon']])
    }

}
