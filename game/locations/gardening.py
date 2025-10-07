from . import GardeningLocation

from game.skills.gardening.plants import *

class CommunityGarden(GardeningLocation):
    description = 'Raised beds where the community gathers to grow fruits and vegetables.'
    plants = [
        Carrot,
        Tomato,
        Potato
    ]

