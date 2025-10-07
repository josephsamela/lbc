from . import CookingLocation

from game.skills.fishing.fish import *
from game.skills.cooking.recipes import *

class CozyCampfire(CookingLocation):
    description = 'Cozy outdoor space where you can prepare & grill fresh-caught fish.'
    recipes = [
        PinkSalmon,
        CohoSalmon,
        SockeyeSalmon,
        ChinookSalmon,
        Cake
    ]
