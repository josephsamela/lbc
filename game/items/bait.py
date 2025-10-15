from . import Item

class Bait(Item):
    def __init__(self, name, cost):
        self.name = name
        self.category = 'live'
        self.cost = cost
        super().__init__(name, self.category)

# LIVE

earthworms = Bait('Earthworms', 1)
mealworms = Bait('Mealworms', 2)
crickets = Bait('Crickets', 4)
blood_worms = Bait('Blood Worms', 4)
glow_worms = Bait('Glow Worms', 5)
cray_fish = Bait('Cray Fish', 6)
sand_flea = Bait('Sand Fleas', 7)
hellgrammites = Bait('Hellgrammites', 8)

live_bait = {
    'earthworms': earthworms,
    'mealworms': mealworms,
    'crickets': crickets,
    'blood_worms': blood_worms,
    'glow_worms': glow_worms,
    'cray_fish': cray_fish,
    'sand_flea': sand_flea,
    'hellgrammites': hellgrammites
}

bait = {
    'live bait': live_bait
}
