from . import CraftingLocation

from game.skills.crafting.recipes.flies import *

class RiverPavilion(CraftingLocation):
    description = 'Covered picnic tables by the river where anglers prepare live bait, lures & flies!'
    recipes = [
        PheasantTail,
        WoolyBugger
    ]
