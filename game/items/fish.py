from .bait import *

class Fish(Item):
    def __init__(self, name, level, bait):
        self.name = name
        self.level = level
        self.xp = level*10
        self.bait = bait
        self.category = "ingredients"
        super().__init__(name, self.category)

# Lake
raw_bluegill = Fish('Raw Bluegill', 1, [earthworms])
raw_pumpkinseed = Fish('Raw Pumpkinseed', 10, [earthworms])
raw_yellow_perch = Fish('Raw Yellow Perch', 20, [earthworms])
raw_smallmouth_bass = Fish('Raw Smallmouth Bass', 30, [earthworms])
raw_walleye = Fish('Raw Walleye', 40, [earthworms])
raw_largemouth_bass = Fish('Raw Largemouth Bass', 50, [earthworms])
raw_chain_pickerel = Fish('Raw Chain Pickerel', 60, [earthworms])
raw_muskellunge = Fish('Raw Muskellunge', 70, [earthworms])
raw_northern_pike = Fish('Raw Northern Pike', 80, [earthworms])
raw_lake_sturgeon = Fish('Raw Lake Sturgeon', 90, [earthworms])
# River
raw_brown_trout = Fish('Raw Brown Trout', 2, [earthworms])
raw_brook_trout = Fish('Raw Brook Trout', 12, [earthworms])
raw_rainbow_trout = Fish('Raw Rainbow Trout', 22, [earthworms])
raw_channel_catfish = Fish('Raw Channel Catfish', 32, [earthworms])
raw_pink_salmon = Fish('Raw Pink Salmon', 42, [earthworms])
raw_chum_salmon = Fish('Raw Chum Salmon', 52, [earthworms])
raw_coho_salmon = Fish('Raw Coho Salmon', 62, [earthworms, mealworms, crickets, blood_worms])
raw_longnose_gar = Fish('Raw Longnose Gar', 72, [earthworms])
raw_sockeye_salmon = Fish('Raw Sockeye Salmon', 82, [earthworms])
raw_chinook_salmon = Fish('Raw Chinook Salmon', 92, [earthworms])
# Ocean
raw_scup = Fish('Raw Scup', 4, [earthworms, mealworms, crickets, blood_worms])
raw_menhaden = Fish('Raw Menhaden', 14, [earthworms])
raw_striped_bass = Fish('Raw Striped Bass', 24, [earthworms])
raw_searobin = Fish('Raw Searobin', 34, [earthworms])
raw_black_seabass = Fish('Raw Black Seabass', 44, [earthworms])
raw_arctic_cod = Fish('Raw Arctic Cod', 54, [earthworms])
raw_bluefish = Fish('Raw Bluefish', 64, [earthworms])
raw_pacific_halibut = Fish('Raw Pacific Halibut', 74, [earthworms])
raw_bluefin_tuna = Fish('Raw Bluefin Tuna', 84, [earthworms])
raw_swordfish = Fish('Raw Swordfish', 94, [earthworms])
# Coral Reef
raw_sergeant_major = Fish('Raw Sergeant Major', 6, [earthworms, mealworms, crickets, blood_worms])
raw_yellowtail_snapper = Fish('Raw Yellowtail Snapper', 16, [earthworms])
raw_spanish_mackerel = Fish('Raw Spanish Mackerel', 26, [earthworms])
raw_goatfish = Fish('Raw Goatfish', 36, [earthworms])
raw_parrotfish = Fish('Raw Parrotfish', 46, [earthworms])
raw_hogfish = Fish('Raw Hogfish', 56, [earthworms])
raw_mahi_mahi = Fish('Raw Mahi Mahi', 66, [earthworms])
raw_red_grouper = Fish('Raw Red Grouper', 76, [earthworms])
raw_giant_trevally = Fish('Raw Giant Trevally', 86, [earthworms])
raw_humphead_wrasse = Fish('Raw Humphead Wrasse', 96, [earthworms])

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
