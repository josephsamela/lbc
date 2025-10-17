from . import *

class CraftingRecipe(Item):
    def __init__(self, name, level, materials, category):
        self.name = name
        self.level = level
        self.xp = level*10
        self.materials = materials
        self.category = category
        super().__init__(self.name, self.category)

class Material(Item):
    def __init__(self, name, cost):
        self.name = name
        self.category = 'materials'
        self.cost = cost
        super().__init__(self.name, self.category)

# Materials
thread = Material('Thread', 1)
bead = Material('Bead', 2)
wire = Material('Wire', 3)
feather = Material('Feather', 4)

hook = Material('Hook', 1)
treble_hook = Material('Treble Hook', 3)

yarn = Material('Yarn', 1)
fur = Material('Fur', 2)
hackle = Material('Hackle', 3)
dubbing = Material('Dubbing', 4)
herl = Material('Herl', 5)
marabou = Material('Marabou', 6)
chenille = Material('Chenille', 7)
flash = Material('Flash', 8)

materials = {
    'common': {
        'thread': thread,
        'bead': bead,
        'wire': wire,
        'feather': feather
    },
    'lure making': {
        'hook': hook,
        'treble_hook': treble_hook
    },
    'fly tying': {
        'yarn': yarn,
        'fur': fur,
        'hackle': hackle,
        'dubbing': dubbing,
        'herl': herl,
        'marabou': marabou,
        'chenille': chenille,
        'flash': flash
    }
}

# Lures
spoon = CraftingRecipe('Spoon', 1, [treble_hook, bead], 'lures')
spinner = CraftingRecipe('Spinner', 10, [treble_hook, feather], 'lures')
jerkbait = CraftingRecipe('Jerkbait', 20, [treble_hook, wire], 'lures')
popper = CraftingRecipe('Popper', 30, [treble_hook, thread], 'lures')
crankbait = CraftingRecipe('Crankbait', 40, [treble_hook, feather], 'lures')
jig = CraftingRecipe('Jig', 50, [treble_hook, feather], 'lures')
swimbait = CraftingRecipe('Swimbait', 60, [treble_hook, feather], 'lures')
topwater = CraftingRecipe('Topwater', 70, [treble_hook, feather], 'lures')

lures = {
    'spoon': spoon,
    'spinner': spinner,
    'jerkbait': jerkbait,
    'popper': popper,
    'crankbait': crankbait,
    'jig': jig,
    'swimbait': swimbait,
    'topwater': topwater
}

# Nymphs
pheasant_tail = CraftingRecipe('Pheasant Tail', 1, [hook, bead, yarn], 'nymphs')
beadhead_prince = CraftingRecipe('Beadhead Prince', 13, [hook, bead, fur], 'nymphs')
biot_midge = CraftingRecipe('Biot Midge', 25, [hook, bead, hackle], 'nymphs')
emerald_tag = CraftingRecipe('Emerald Tag', 37, [hook, bead, dubbing], 'nymphs')
zebra_midge = CraftingRecipe('Zebra Midge', 49, [hook, bead, herl], 'nymphs')
gold_hunchback = CraftingRecipe('Gold Hunchback', 61, [hook, bead, marabou], 'nymphs')
tungsten_dart = CraftingRecipe('Tungsten Dart', 73, [hook, bead, chenille], 'nymphs')
golden_walts = CraftingRecipe('Golden Walts', 85, [hook, bead, flash], 'nymphs')

# Dry Flies
blue_dun = CraftingRecipe('Blue Dun', 4, [hook, thread, yarn], 'dry flies')
parachute_adams = CraftingRecipe('Parachute Adams', 16, [hook, thread, fur], 'dry flies')
green_drake = CraftingRecipe('Green Drake', 28, [hook, thread, hackle], 'dry flies')
wiggle_damsel = CraftingRecipe('Wiggle Damsel', 40, [hook, thread, dubbing], 'dry flies')
amber_crane = CraftingRecipe('Amber Crane', 52, [hook, thread, herl], 'dry flies')
royal_wulff = CraftingRecipe('Royal Wulff', 64, [hook, thread, marabou], 'dry flies')
clark_cicada = CraftingRecipe('Clark Cicada', 76, [hook, thread, chenille], 'dry flies')
olive_quill = CraftingRecipe('Olive Quill', 88, [hook, thread, flash], 'dry flies')

# Wet Flies
royal_coachman = CraftingRecipe('Royal Coachman', 7, [hook, wire, yarn], 'wet flies')
soft_hackle = CraftingRecipe('Soft Hackle', 19, [hook, wire, fur], 'wet flies')
jimmy_starling = CraftingRecipe('Jimmy Starling', 31, [hook, wire, hackle], 'wet flies')
fontinalis_fin = CraftingRecipe('Fontinalis Fin', 43, [hook, wire, dubbing], 'wet flies')
grizzly_king = CraftingRecipe('Grizzly King', 55, [hook, wire, herl], 'wet flies')
pink_lady = CraftingRecipe('Pink Lady', 67, [hook, wire, marabou], 'wet flies')
catskill_striker = CraftingRecipe('Catskill Striker', 79, [hook, wire, chenille], 'wet flies')
pamachene_belle = CraftingRecipe('Pamachene Belle', 91, [hook, wire, flash], 'wet flies')

# Streamers
wooly_bugger = CraftingRecipe('Wooly Bugger', 10, [hook, feather, yarn], 'streamers')
mickey_finn = CraftingRecipe('Mickey Finn', 21, [hook, feather, fur], 'streamers')
ashdown_green = CraftingRecipe('Ashdown Green', 34, [hook, feather, hackle], 'streamers')
black_conehead = CraftingRecipe('Black Conehead', 46, [hook, feather, dubbing], 'streamers')
red_mudder = CraftingRecipe('Red Mudder', 58, [hook, feather, herl], 'streamers')
clouser_minnow = CraftingRecipe('Clouser Minnow', 70, [hook, feather, marabou], 'streamers')
crimson_duke = CraftingRecipe('Crimson Duke', 82, [hook, feather, chenille], 'streamers')
amber_scourge = CraftingRecipe('Amber Scourge', 94, [hook, feather, flash], 'streamers')

nymphs = {
    'pheasant_tail': pheasant_tail,
    'beadhead_prince': beadhead_prince,
    'biot_midge': biot_midge,
    'emerald_tag': emerald_tag,
    'zebra_midge': zebra_midge,
    'gold_hunchback': gold_hunchback,
    'tungsten_dart': tungsten_dart,
    'golden_walts': golden_walts
}

dry_flies = {
    'blue_dun': blue_dun,
    'parachute_adams': parachute_adams,
    'green_drake': green_drake,
    'wiggle_damsel': wiggle_damsel,
    'amber_crane': amber_crane,
    'royal_wulff': royal_wulff,
    'clark_cicada': clark_cicada,
    'olive_quill': olive_quill
}

wet_flies = {
    'royal_coachman': royal_coachman,
    'soft_hackle': soft_hackle,
    'jimmy_starling': jimmy_starling,
    'fontinalis_fin': fontinalis_fin,
    'grizzly_king': grizzly_king,
    'pink_lady': pink_lady,
    'catskill_striker': catskill_striker,
    'pamachene_belle': pamachene_belle
}

streamers = {
    'wooly_bugger': wooly_bugger,
    'mickey_finn': mickey_finn,
    'ashdown_green': ashdown_green,
    'black_conehead': black_conehead,
    'red_mudder': red_mudder,
    'clouser_minnow': clouser_minnow,
    'crimson_duke': crimson_duke,
    'amber_scourge': amber_scourge
}

flies = {
    'nymphs': nymphs,
    'dry flies': dry_flies,
    'wet flies': wet_flies,
    'streamers': streamers
}

crafting_recipes = {
    'lures': lures,
    'nymphs': nymphs,
    'dry flies': dry_flies,
    'wet flies': wet_flies,
    'streamers': streamers
}
