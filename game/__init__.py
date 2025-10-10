from .actions.fishing import FishAction
from .actions.cooking import CookAction
from .actions.crafting import CraftAction

from .items import *

class Game:
    def __init__(self):
        self.skills = {
            "fishing": {
                "name": "Fishing",
                "description": "Explore lakes, rivers and oceans to fish exciting locations and discover new species!",
                "resources": [
                    raw_pink_salmon,
                    raw_coho_salmon,
                    raw_sockeye_salmon,
                    raw_chinook_salmon
                ]
            },
            "gardening": {
                "name": "Gardening",
                "description": "Grab your rod and tackle! Come join your fellow anglers to go fishing!",
                "resources": []
            },
            "cooking": {
                "name": "Cooking",
                "description": "Grab your rod and tackle! Come join your fellow anglers to go fishing!",
                "resources": [
                    cake
                ]
            },
            "crafting": {
                "name": "Crafting",
                "description": "Gather materials and use your crafting skill to ",
                "resources": [
                    pheasant_tail
                ]
            }
        }

        self.locations = {
            "fishing": {
                "tributary_river": {
                    "actions": [
                        FishAction([
                            raw_pink_salmon,
                            raw_coho_salmon,
                            raw_sockeye_salmon,
                            raw_chinook_salmon
                        ])
                    ]
                }
            }
        }

    journal = {
        'fish': {
            'skill': 'fishing',
            'salmon': [
                raw_pink_salmon,
                raw_coho_salmon,
                raw_sockeye_salmon,
                raw_chinook_salmon
            ],
            'trout': [
                raw_brown_trout,
                raw_brook_trout,
                raw_rainbow_trout
            ]
        },
        'plants': {
            'skill': 'gardening',
            'vegetables': [
                cake
            ]
        },
        'recipes': {
            'skill': 'cooking',
            'desserts': [
                cake
            ]
        },
        'bait': {
            'skill': 'crafting',
            'lures': [
                crankbait
            ],
            'flies': [
                pheasant_tail
            ]
        }
    }
