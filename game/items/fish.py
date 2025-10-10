from . import *

class Fish(Item):
    def __init__(self, name, level, bait):
        self.name = name
        self.level = level
        self.xp = level*10
        self.bait = bait
        super().__init__(name)

raw_pink_salmon = Fish('Raw Pink Salmon', 1, [nightcrawlers])
raw_coho_salmon = Fish('Raw Coho Salmon', 5, [meal_worms])
raw_sockeye_salmon = Fish('Raw Sockeye Salmon', 10, [crickets])
raw_chinook_salmon = Fish('Raw Chinook Salmon', 20, [blood_worms])

raw_brown_trout = Fish('Raw Brown Trout', 1, [nightcrawlers])
raw_brook_trout = Fish('Raw Brook Trout', 5, [meal_worms])
raw_rainbow_trout = Fish('Raw Rainbow Trout', 10, [crickets])
