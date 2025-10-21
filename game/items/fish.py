from .bait import *
from .crafting_recipes import *

class Fish(Item):
    def __init__(self, name, level, bait):
        self.name = name
        self.level = level
        self.xp = level*10
        self.bait = bait
        self.category = "ingredients"
        super().__init__(name, self.category)

# Lake
raw_bluegill = Fish('Raw Bluegill', 1, [earthworms, spoon, pheasant_tail])
raw_pumpkinseed = Fish('Raw Pumpkinseed', 10, [earthworms, spinner, wooly_bugger])
raw_yellow_perch = Fish('Raw Yellow Perch', 20, [mealworms, jerkbait, soft_hackle])
raw_smallmouth_bass = Fish('Raw Smallmouth Bass', 30, [mealworms, popper, green_drake])
raw_walleye = Fish('Raw Walleye', 40, [crickets, crankbait, wiggle_damsel])
raw_largemouth_bass = Fish('Raw Largemouth Bass', 50, [crickets,jig, zebra_midge])
raw_chain_pickerel = Fish('Raw Chain Pickerel', 60, [blood_worms, swimbait, red_mudder])
raw_muskellunge = Fish('Raw Muskellunge', 70, [blood_worms, topwater, clouser_minnow])
raw_northern_pike = Fish('Raw Northern Pike', 80, [glow_worms, catskill_striker])
raw_lake_sturgeon = Fish('Raw Lake Sturgeon', 90, [glow_worms, pamachene_belle])
# River
raw_brown_trout = Fish('Raw Brown Trout', 2, [mealworms, spoon, pheasant_tail])
raw_brook_trout = Fish('Raw Brook Trout', 12, [mealworms, spinner, wooly_bugger])
raw_rainbow_trout = Fish('Raw Rainbow Trout', 22, [crickets, jerkbait, mickey_finn])
raw_channel_catfish = Fish('Raw Channel Catfish', 32, [crickets, popper, jimmy_starling])
raw_pink_salmon = Fish('Raw Pink Salmon', 42, [blood_worms, crankbait, fontinalis_fin])
raw_chum_salmon = Fish('Raw Chum Salmon', 52, [blood_worms, jig, amber_crane])
raw_coho_salmon = Fish('Raw Coho Salmon', 62, [glow_worms, swimbait, gold_hunchback])
raw_longnose_gar = Fish('Raw Longnose Gar', 72, [glow_worms, topwater, tungsten_dart])
raw_sockeye_salmon = Fish('Raw Sockeye Salmon', 82, [cray_fish, crimson_duke])
raw_chinook_salmon = Fish('Raw Chinook Salmon', 92, [cray_fish, ashdown_green])
# Ocean
raw_scup = Fish('Raw Scup', 4, [crickets, spoon, blue_dun])
raw_menhaden = Fish('Raw Menhaden', 14, [crickets, spinner, beadhead_prince])
raw_striped_bass = Fish('Raw Striped Bass', 24, [blood_worms, jerkbait, biot_midge])
raw_searobin = Fish('Raw Searobin', 34, [blood_worms, popper, royal_coachman])
raw_black_seabass = Fish('Raw Black Seabass', 44, [glow_worms, crankbait, fontinalis_fin])
raw_arctic_cod = Fish('Raw Arctic Cod', 54, [glow_worms, jig, grizzly_king])
raw_bluefish = Fish('Raw Bluefish', 64, [cray_fish, swimbait, royal_wulff])
raw_pacific_halibut = Fish('Raw Pacific Halibut', 74, [cray_fish, tungsten_dart])
raw_bluefin_tuna = Fish('Raw Bluefin Tuna', 84, [sand_fleas, topwater, golden_walts])
raw_swordfish = Fish('Raw Swordfish', 94, [sand_fleas, ashdown_green])
# Coral Reef
raw_sergeant_major = Fish('Raw Sergeant Major', 6, [blood_worms, spoon, royal_coachman])
raw_yellowtail_snapper = Fish('Raw Yellowtail Snapper', 16, [blood_worms, spinner, parachute_adams])
raw_spanish_mackerel = Fish('Raw Spanish Mackerel', 26, [glow_worms, jerkbait, biot_midge])
raw_goatfish = Fish('Raw Goatfish', 36, [glow_worms, popper, emerald_tag])
raw_parrotfish = Fish('Raw Parrotfish', 46, [cray_fish, crankbait, black_conehead])
raw_hogfish = Fish('Raw Hogfish', 56, [cray_fish, jig, grizzly_king])
raw_mahi_mahi = Fish('Raw Mahi Mahi', 66, [sand_fleas, swimbait, pink_lady])
raw_red_grouper = Fish('Raw Red Grouper', 76, [sand_fleas, topwater, clark_cicada])
raw_giant_trevally = Fish('Raw Giant Trevally', 86, [hellgrammites, olive_quill])
raw_humphead_wrasse = Fish('Raw Humphead Wrasse', 96, [hellgrammites, pamachene_belle])

lake = {
    'raw_bluegill': raw_bluegill,
    'raw_pumpkinseed': raw_pumpkinseed,
    'raw_yellow_perch': raw_yellow_perch,
    'raw_smallmouth_bass': raw_smallmouth_bass,
    'raw_walleye': raw_walleye,
    'raw_largemouth_bass': raw_largemouth_bass,
    'raw_chain_pickerel': raw_chain_pickerel,
    'raw_muskellunge': raw_muskellunge,
    'raw_northern_pike': raw_northern_pike,
    'raw_lake_sturgeon': raw_lake_sturgeon
}

river = {
    'raw_brown_trout': raw_brown_trout,
    'raw_brook_trout': raw_brook_trout,
    'raw_rainbow_trout': raw_rainbow_trout,
    'raw_channel_catfish': raw_channel_catfish,
    'raw_pink_salmon': raw_pink_salmon,
    'raw_chum_salmon': raw_chum_salmon,
    'raw_coho_salmon': raw_coho_salmon,
    'raw_longnose_gar': raw_longnose_gar,
    'raw_sockeye_salmon': raw_sockeye_salmon,
    'raw_chinook_salmon': raw_chinook_salmon
}

ocean = {
    'raw_scup': raw_scup,
    'raw_menhaden': raw_menhaden,
    'raw_striped_bass': raw_striped_bass,
    'raw_searobin': raw_searobin,
    'raw_black_seabass': raw_black_seabass,
    'raw_arctic_cod': raw_arctic_cod,
    'raw_bluefish': raw_bluefish,
    'raw_pacific_halibut': raw_pacific_halibut,
    'raw_bluefin_tuna': raw_bluefin_tuna,
    'raw_swordfish': raw_swordfish
}

coral_reef = {
    'raw_sergeant_major': raw_sergeant_major,
    'raw_yellowtail_snapper': raw_yellowtail_snapper,
    'raw_spanish_mackerel': raw_spanish_mackerel,
    'raw_goatfish': raw_goatfish,
    'raw_parrotfish': raw_parrotfish,
    'raw_hogfish': raw_hogfish,
    'raw_mahi_mahi': raw_mahi_mahi,
    'raw_red_grouper': raw_red_grouper,
    'raw_giant_trevally': raw_giant_trevally,
    'raw_humphead_wrasse': raw_humphead_wrasse
}

fish = {
    'lake': lake,
    'river': river,
    'ocean': ocean,
    'coral reef': coral_reef
}
