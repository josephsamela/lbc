from . import Item

class Bait(Item):
    def __init__(self, name):
        self.name = name
        super().__init__(name)

nightcrawlers = Bait('Nightcrawlers')
meal_worms    = Bait('Meal Worms')
crickets      = Bait('Crickets')
blood_worms   = Bait('Blood Worms')
