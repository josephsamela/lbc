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

crafting_recipes = {
    'skill': 'crafting',
    'lures': {
        'crankbait': CraftingRecipe('Crankbait', 1, [bead, feather, wire]),
        'popper': CraftingRecipe('Popper', 1, [bead, feather, wire]),
        'spoon': CraftingRecipe('Spoon', 1, [bead, feather, wire]),
        'spinner': CraftingRecipe('Spinner', 1, [bead, feather, wire]),
        'jig': CraftingRecipe('Jig', 1, [bead, feather, wire]),
        'jerkbait': CraftingRecipe('Jerkbait', 1, [bead, feather, wire]),
        'swimbait': CraftingRecipe('Swimbait', 1, [bead, feather, wire]),
        'topwater': CraftingRecipe('Topwater', 1, [bead, feather, wire])
    },
    'flies': {
        # Nymphs
        'pheasant_tail': CraftingRecipe('Pheasant Tail', 1, [bead, feather, wire]),
        'beadhead_prince': CraftingRecipe('Beadhead Prince', 13, [bead, feather, wire]),
        'biot_midge': CraftingRecipe('Biot Midge', 25, [bead, feather, wire]),
        'emerald_tag': CraftingRecipe('Emerald Tag', 37, [bead, feather, wire]),
        'zebra_midge': CraftingRecipe('Zebra Midge', 49, [bead, feather, wire]),
        'gold_hunchback': CraftingRecipe('Gold Hunchback', 61, [bead, feather, wire]),
        'tungsten_dart': CraftingRecipe('Tungsten Dart', 73, [bead, feather, wire]),
        'golden_walts': CraftingRecipe('Golden Walts', 85, [bead, feather, wire]),

        # Dry Flies
        'blue_dun': CraftingRecipe('Blue Dun', 4, [bead, feather, wire]),
        'parachute_adams': CraftingRecipe('Parachute Adams', 16, [bead, feather, wire]),
        'green_drake': CraftingRecipe('Green Drake', 28, [bead, feather, wire]),
        'wiggle_damsel': CraftingRecipe('Wiggle Damsel', 40, [bead, feather, wire]),
        'amber_crane': CraftingRecipe('Amber Crane', 52, [bead, feather, wire]),
        'royal_wulff': CraftingRecipe('Royal Wulff', 64, [bead, feather, wire]),
        'clark_cicada': CraftingRecipe('Clark Cicada', 76, [bead, feather, wire]),
        'olive_quill': CraftingRecipe('Olive Quill', 88, [bead, feather, wire]),

        # Wet Flies
        'royal_coachman': CraftingRecipe('Royal Coachman', 7, [bead, feather, wire]),
        'soft_hackle': CraftingRecipe('Soft Hackle', 19, [bead, feather, wire]),
        'jimmy_starling': CraftingRecipe('Jimmy Starling', 31, [bead, feather, wire]),
        'fontinalis_fin': CraftingRecipe('Fontinalis Fin', 43, [bead, feather, wire]),
        'grizzly_king': CraftingRecipe('Grizzly King', 55, [bead, feather, wire]),
        'pink_lady': CraftingRecipe('Pink Lady', 67, [bead, feather, wire]),
        'catskill_striker': CraftingRecipe('Catskill Striker', 79, [bead, feather, wire]),
        'pamachene_belle': CraftingRecipe('Pamachene Belle', 91, [bead, feather, wire]),

        # Streamers
        'wooly_bugger': CraftingRecipe('Wooly Bugger', 10, [bead, feather, wire]),
        'mickey_finn': CraftingRecipe('Mickey Finn', 21, [bead, feather, wire]),
        'ashdown_green': CraftingRecipe('Ashdown Green', 34, [bead, feather, wire]),
        'black_conehead': CraftingRecipe('Black Conehead', 46, [bead, feather, wire]),
        'red_mudder': CraftingRecipe('Red Mudder', 58, [bead, feather, wire]),
        'clouser_minnow': CraftingRecipe('Clouser Minnow', 70, [bead, feather, wire]),
        'crimson_duke': CraftingRecipe('Crimson Duke', 82, [bead, feather, wire]),
        'amber_scourge': CraftingRecipe('Amber Scourge', 94, [bead, feather, wire])
    }
}
