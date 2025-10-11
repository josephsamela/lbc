from . import *

class Fish(Item):
    def __init__(self, name, level, bait):
        self.name = name
        self.level = level
        self.xp = level*10
        self.bait = bait
        super().__init__(name)

# LAKES
raw_bluegill = Fish('Raw Bluegill', 1, [nightcrawlers])
raw_pumpkinseed = Fish('Raw Pumpkinseed', 10, [nightcrawlers])
raw_yellow_perch = Fish('Raw Yellow Perch', 20, [nightcrawlers])
raw_smallmouth_bass = Fish('Raw Smallmouth Bass', 30, [nightcrawlers])
raw_walleye = Fish('Raw Walleye', 40, [nightcrawlers])
raw_largemouth_bass = Fish('Raw Largemouth Bass', 50, [nightcrawlers])
raw_chain_pickerel = Fish('Raw Chain Pickerel', 60, [nightcrawlers])
raw_muskellunge = Fish('Raw Muskellunge', 70, [nightcrawlers])
raw_northern_pike = Fish('Raw Northern Pike', 80, [nightcrawlers])
raw_lake_sturgeon = Fish('Raw Lake Sturgeon', 90, [nightcrawlers])

# RIVERS
raw_brown_trout = Fish('Raw Brown Trout', 2, [nightcrawlers])
raw_brook_trout = Fish('Raw Brook Trout', 12, [nightcrawlers])
raw_rainbow_trout = Fish('Raw Rainbow Trout', 22, [nightcrawlers])
raw_channel_catfish = Fish('Raw Channel Catfish', 32, [nightcrawlers])
raw_pink_salmon = Fish('Raw Pink Salmon', 42, [nightcrawlers])
raw_chum_salmon = Fish('Raw Chum Salmon', 52, [nightcrawlers])
raw_coho_salmon = Fish('Raw Coho Salmon', 62, [nightcrawlers, meal_worms, crickets, blood_worms])
raw_longnose_gar = Fish('Raw Longnose Gar', 72, [nightcrawlers])
raw_sockeye_salmon = Fish('Raw Sockeye Salmon', 82, [nightcrawlers])
raw_chinook_salmon = Fish('Raw Chinook Salmon', 92, [nightcrawlers])

# OCEANS
raw_scup = Fish('Raw Scup', 4, [nightcrawlers])
raw_menhaden = Fish('Raw Menhaden', 14, [nightcrawlers])
raw_striped_bass = Fish('Raw Striped Bass', 24, [nightcrawlers])
raw_searobin = Fish('Raw Searobin', 34, [nightcrawlers])
raw_black_seabass = Fish('Raw Black Seabass', 44, [nightcrawlers])
raw_arctic_cod = Fish('Raw Arctic Cod', 54, [nightcrawlers])
raw_bluefish = Fish('Raw Bluefish', 64, [nightcrawlers])
raw_pacific_halibut = Fish('Raw Pacific Halibut', 74, [nightcrawlers])
raw_bluefin_tuna = Fish('Raw Bluefin Tuna', 84, [nightcrawlers])
raw_swordfish = Fish('Raw Swordfish', 94, [nightcrawlers])

# CORAL REEF
raw_sergeant_major = Fish('Raw Sergeant Major', 6, [nightcrawlers])
raw_yellowtail_snapper = Fish('Raw Yellowtail Snapper', 16, [nightcrawlers])
raw_spanish_mackerel = Fish('Raw Spanish Mackerel', 26, [nightcrawlers])
raw_goatfish = Fish('Raw Goatfish', 36, [nightcrawlers])
raw_parrotfish = Fish('Raw Parrotfish', 46, [nightcrawlers])
raw_hogfish = Fish('Raw Hogfish', 56, [nightcrawlers])
raw_mahi_mahi = Fish('Raw Mahi Mahi', 66, [nightcrawlers])
raw_red_grouper = Fish('Raw Red Grouper', 76, [nightcrawlers])
raw_giant_trevally = Fish('Raw Giant Trevally', 86, [nightcrawlers])
raw_humphead_wrasse = Fish('Raw Humphead Wrasse', 96, [nightcrawlers])
