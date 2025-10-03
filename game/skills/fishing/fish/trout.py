from . import Fish
from ..bait import *

class Trout(Fish):
    required_bait = [Nightcrawlers, Mealworms, Crankbait, Spinner]

class BrownTrout(Trout):
    required_level = 0
    xp = 10

class BrookTrout(Trout):
    required_level = 5
    xp = 20

class RainbowTrout(Trout):
    required_level = 10
    xp = 30
