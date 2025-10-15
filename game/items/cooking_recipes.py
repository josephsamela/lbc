from . import *

from .fish import *

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

cooked_fish = {
    'cooked fish': {
        'cooked_bluegill': CookingRecipe('Cooked Bluegill', 'Burnt Bluegill', 1, [raw_bluegill]),
        'cooked_brown_trout': CookingRecipe('Cooked Brown Trout', 'Burnt Brown Trout', 2, [raw_brown_trout]),
        'cooked_scup': CookingRecipe('Cooked Scup', 'Burnt Scup', 4, [raw_scup]),
        'cooked_sergeant_major': CookingRecipe('Cooked Sergeant Major', 'Burnt Sergeant Major', 6, [raw_sergeant_major]),        
        'cooked_pumpkinseed': CookingRecipe('Cooked Pumpkinseed', 'Burnt Pumpkinseed', 10, [raw_pumpkinseed]),
        'cooked_brook_trout': CookingRecipe('Cooked Brook Trout', 'Burnt Brook Trout', 12, [raw_brook_trout]),
        'cooked_menhaden': CookingRecipe('Cooked Menhaden', 'Burnt Menhaden', 14, [raw_menhaden]),
        'cooked_yellowtail_snapper': CookingRecipe('Cooked Yellowtail Snapper', 'Burnt Yellowtail Snapper', 16, [raw_yellowtail_snapper]),
        'cooked_yellow_perch': CookingRecipe('Cooked Yellow Perch', 'Burnt Yellow Perch', 20, [raw_yellow_perch]),
        'cooked_rainbow_trout': CookingRecipe('Cooked Rainbow Trout', 'Burnt Rainbow Trout', 22, [raw_rainbow_trout]),
        'cooked_striped_bass': CookingRecipe('Cooked Striped Bass', 'Burnt Striped Bass', 24, [raw_striped_bass]),
        'cooked_spanish_mackerel': CookingRecipe('Cooked Spanish Mackerel', 'Burnt Spanish Mackerel', 26, [raw_spanish_mackerel]),
        'cooked_smallmouth_bass': CookingRecipe('Cooked Smallmouth Bass', 'Burnt Smallmouth Bass', 30, [raw_smallmouth_bass]),
        'cooked_channel_catfish': CookingRecipe('Cooked Channel Catfish', 'Burnt Channel Catfish', 32, [raw_channel_catfish]),
        'cooked_searobin': CookingRecipe('Cooked Searobin', 'Burnt Searobin', 34, [raw_searobin]),
        'cooked_goatfish': CookingRecipe('Cooked Goatfish', 'Burnt Goatfish', 36, [raw_goatfish]),
        'cooked_walleye': CookingRecipe('Cooked Walleye', 'Burnt Walleye', 40, [raw_walleye]),
        'cooked_pink_salmon': CookingRecipe('Cooked Pink Salmon', 'Burnt Pink Salmon', 42, [raw_pink_salmon]),
        'cooked_black_seabass': CookingRecipe('Cooked Black Seabass', 'Burnt Black Seabass', 44, [raw_black_seabass]),
        'cooked_parrotfish': CookingRecipe('Cooked Parrotfish', 'Burnt Parrotfish', 46, [raw_parrotfish]),
        'cooked_largemouth_bass': CookingRecipe('Cooked Largemouth Bass', 'Burnt Largemouth Bass', 50, [raw_largemouth_bass]),
        'cooked_chum_salmon': CookingRecipe('Cooked Chum Salmon', 'Burnt Chum Salmon', 52, [raw_chum_salmon]),
        'cooked_arctic_cod': CookingRecipe('Cooked Arctic Cod', 'Burnt Arctic Cod', 54, [raw_arctic_cod]),
        'cooked_hogfish': CookingRecipe('Cooked Hogfish', 'Burnt Hogfish', 56, [raw_hogfish]),
        'cooked_chain_pickerel': CookingRecipe('Cooked Chain Pickerel', 'Burnt Chain Pickerel', 60, [raw_chain_pickerel]),
        'cooked_coho_salmon': CookingRecipe('Cooked Coho Salmon', 'Burnt Coho Salmon', 62, [raw_coho_salmon]),
        'cooked_bluefish': CookingRecipe('Cooked Bluefish', 'Burnt Bluefish', 64, [raw_bluefish]),
        'cooked_mahi_mahi': CookingRecipe('Cooked Mahi Mahi', 'Burnt Mahi Mahi', 66, [raw_mahi_mahi]),
        'cooked_muskellunge': CookingRecipe('Cooked Muskellunge', 'Burnt Muskellunge', 70, [raw_muskellunge]),
        'cooked_longnose_gar': CookingRecipe('Cooked Longnose Gar', 'Burnt Longnose Gar', 72, [raw_longnose_gar]),
        'cooked_pacific_halibut': CookingRecipe('Cooked Pacific Halibut', 'Burnt Pacific Halibut', 74, [raw_pacific_halibut]),
        'cooked_red_grouper': CookingRecipe('Cooked Red Grouper', 'Burnt Red Grouper', 76, [raw_red_grouper]),
        'cooked_northern_pike': CookingRecipe('Cooked Northern Pike', 'Burnt Northern Pike', 80, [raw_northern_pike]),
        'cooked_sockeye_salmon': CookingRecipe('Cooked Sockeye Salmon', 'Burnt Sockeye Salmon', 82, [raw_sockeye_salmon]),
        'cooked_bluefin_tuna': CookingRecipe('Cooked Bluefin Tuna', 'Burnt Bluefin Tuna', 84, [raw_bluefin_tuna]),
        'cooked_giant_trevally': CookingRecipe('Cooked Giant Trevally', 'Burnt Giant Trevally', 86, [raw_giant_trevally]),
        'cooked_lake_sturgeon': CookingRecipe('Cooked Lake Sturgeon', 'Burnt Lake Sturgeon', 90, [raw_lake_sturgeon]),
        'cooked_chinook_salmon': CookingRecipe('Cooked Chinook Salmon', 'Burnt Chinook Salmon', 92, [raw_chinook_salmon]),
        'cooked_swordfish': CookingRecipe('Cooked Swordfish', 'Burnt Swordfish', 94, [raw_swordfish]),
        'cooked_humphead_wrasse': CookingRecipe('Cooked Humphead Wrasse', 'Burnt Humphead Wrasse', 96, [raw_humphead_wrasse])
    }
}

cooking_recipes = {
    'cooked_fish': cooked_fish
}
