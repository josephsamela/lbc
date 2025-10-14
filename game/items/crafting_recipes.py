from . import *

class CraftingRecipe(Item):
    def __init__(self, name, level, materials, category):
        self.name = name
        self.level = level
        self.xp = level*10
        self.materials = materials
        self.category = category
        super().__init__(self.name, self.category)

# Materials
bead = Item('Bead', 'materials')
feather = Item('Feather', 'materials')
wire = Item('Wire', 'materials')

lures = {
    'crankbait': CraftingRecipe('Crankbait', 1, [bead, feather, wire], 'lures'),
    'popper': CraftingRecipe('Popper', 1, [bead, feather, wire], 'lures'),
    'spoon': CraftingRecipe('Spoon', 1, [bead, feather, wire], 'lures'),
    'spinner': CraftingRecipe('Spinner', 1, [bead, feather, wire], 'lures'),
    'jig': CraftingRecipe('Jig', 1, [bead, feather, wire], 'lures'),
    'jerkbait': CraftingRecipe('Jerkbait', 1, [bead, feather, wire], 'lures'),
    'swimbait': CraftingRecipe('Swimbait', 1, [bead, feather, wire], 'lures'),
    'topwater': CraftingRecipe('Topwater', 1, [bead, feather, wire], 'lures')
}

flies = {
    'nymphs': {
        'pheasant_tail': CraftingRecipe('Pheasant Tail', 1, [bead, feather, wire], 'nymphs'),
        'beadhead_prince': CraftingRecipe('Beadhead Prince', 13, [bead, feather, wire], 'nymphs'),
        'biot_midge': CraftingRecipe('Biot Midge', 25, [bead, feather, wire], 'nymphs'),
        'emerald_tag': CraftingRecipe('Emerald Tag', 37, [bead, feather, wire], 'nymphs'),
        'zebra_midge': CraftingRecipe('Zebra Midge', 49, [bead, feather, wire], 'nymphs'),
        'gold_hunchback': CraftingRecipe('Gold Hunchback', 61, [bead, feather, wire], 'nymphs'),
        'tungsten_dart': CraftingRecipe('Tungsten Dart', 73, [bead, feather, wire], 'nymphs'),
        'golden_walts': CraftingRecipe('Golden Walts', 85, [bead, feather, wire], 'nymphs'),
    },
    'dry flies': {
        'blue_dun': CraftingRecipe('Blue Dun', 4, [bead, feather, wire], 'dry flies'),
        'parachute_adams': CraftingRecipe('Parachute Adams', 16, [bead, feather, wire], 'dry flies'),
        'green_drake': CraftingRecipe('Green Drake', 28, [bead, feather, wire], 'dry flies'),
        'wiggle_damsel': CraftingRecipe('Wiggle Damsel', 40, [bead, feather, wire], 'dry flies'),
        'amber_crane': CraftingRecipe('Amber Crane', 52, [bead, feather, wire], 'dry flies'),
        'royal_wulff': CraftingRecipe('Royal Wulff', 64, [bead, feather, wire], 'dry flies'),
        'clark_cicada': CraftingRecipe('Clark Cicada', 76, [bead, feather, wire], 'dry flies'),
        'olive_quill': CraftingRecipe('Olive Quill', 88, [bead, feather, wire], 'dry flies'),
    },
    'wet flies': {
        'royal_coachman': CraftingRecipe('Royal Coachman', 7, [bead, feather, wire], 'wet flies'),
        'soft_hackle': CraftingRecipe('Soft Hackle', 19, [bead, feather, wire], 'wet flies'),
        'jimmy_starling': CraftingRecipe('Jimmy Starling', 31, [bead, feather, wire], 'wet flies'),
        'fontinalis_fin': CraftingRecipe('Fontinalis Fin', 43, [bead, feather, wire], 'wet flies'),
        'grizzly_king': CraftingRecipe('Grizzly King', 55, [bead, feather, wire], 'wet flies'),
        'pink_lady': CraftingRecipe('Pink Lady', 67, [bead, feather, wire], 'wet flies'),
        'catskill_striker': CraftingRecipe('Catskill Striker', 79, [bead, feather, wire], 'wet flies'),
        'pamachene_belle': CraftingRecipe('Pamachene Belle', 91, [bead, feather, wire], 'wet flies'),
    },
    'streamers': {
        'wooly_bugger': CraftingRecipe('Wooly Bugger', 10, [bead, feather, wire], 'streamers'),
        'mickey_finn': CraftingRecipe('Mickey Finn', 21, [bead, feather, wire], 'streamers'),
        'ashdown_green': CraftingRecipe('Ashdown Green', 34, [bead, feather, wire], 'streamers'),
        'black_conehead': CraftingRecipe('Black Conehead', 46, [bead, feather, wire], 'streamers'),
        'red_mudder': CraftingRecipe('Red Mudder', 58, [bead, feather, wire], 'streamers'),
        'clouser_minnow': CraftingRecipe('Clouser Minnow', 70, [bead, feather, wire], 'streamers'),
        'crimson_duke': CraftingRecipe('Crimson Duke', 82, [bead, feather, wire], 'streamers'),
        'amber_scourge': CraftingRecipe('Amber Scourge', 94, [bead, feather, wire], 'streamers')
    }
}

crafting_recipes = {
    'flies': flies,
    'lures': lures
}
