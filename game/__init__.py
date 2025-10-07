from .skills import *

class Game:
    skills = {
        'fishing': Fishing(),
        'gardening': Gardening(),
        'cooking': Cooking(),
        'crafting': Crafting()
    }
