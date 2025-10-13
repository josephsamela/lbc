from . import Item

class Bait(Item):
    def __init__(self, name):
        self.name = name
        self.category = 'live'
        super().__init__(name, self.category)

# LIVE

earthworms = Bait('Earthworms')
mealworms = Bait('Mealworms')
crickets = Bait('Crickets')
blood_worms = Bait('Blood Worms')
glow_worms = Bait('Glow Worms')
cray_fish = Bait('Cray Fish')
sand_flea = Bait('Sand Fleas')
hellgrammites = Bait('Hellgrammites')

bait = {
    'live': {
        'earthworms': earthworms,
        'mealworms': mealworms,
        'crickets': crickets,
        'blood_worms': blood_worms,
        'glow_worms': glow_worms,
        'cray_fish': cray_fish,
        'sand_flea': sand_flea,
        'hellgrammites': hellgrammites
    }
}
