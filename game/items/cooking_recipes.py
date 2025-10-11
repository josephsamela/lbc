from . import *

class CookingRecipe(Item):
    def __init__(self, name_success, name_failure, level, ingredients, xp_bonus=10):
        self.name = name_success
        self.level = level
        self.xp = level*xp_bonus
        self.ingredients = ingredients
        self.burnt = Item(name_failure)
        super().__init__(self.name)

# Ingredients
flour = Item('Flour')
egg = Item('Egg')
milk = Item('Milk')

# Deserts
cake = CookingRecipe('Cake', 'Burnt Cake', 1, [flour, egg, milk], xp_bonus=100)

# Fish
# cooked_pink_salmon = CookingRecipe('Cooked Pink Salmon', 'Burnt Pink Salmon', 1, [raw_pink_salmon])
# cooked_coho_salmon = CookingRecipe('Cooked Coho Salmon', 'Burnt Coho Salmon', 1, [raw_coho_salmon])
# cooked_sockeye_salmon = CookingRecipe('Cooked Sockeye Salmon', 'Burnt Sockeye Salmon', 1, [raw_sockeye_salmon])
# cooked_chinook_salmon = CookingRecipe('Cooked Chinook Salmon', 'Burnt Chinook Salmon', 1, [raw_chinook_salmon])
