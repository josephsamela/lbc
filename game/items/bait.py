from . import Item

class Bait(Item):
    pass

class Nightcrawlers(Bait):
    name = 'Nightcrawlers'

class Mealworms(Bait):
    name = 'Mealworms'

class Crickets(Bait):
    name = 'Crickets'

class Baits():
    nightcrawlers = Nightcrawlers
    mealworms = Mealworms
    crickets = Crickets
