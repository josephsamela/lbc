from .actions.fishing import FishAction
from .actions.cooking import CookAction
from .actions.crafting import CraftAction

from .items import *

class Game:
    def __init__(self):
        self.skills = {
            "fishing": {
                "name": "Fishing",
                "description": "Grab your rod and tackle! Come join your fellow anglers to go fishing!",
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
                "resources": []
            },
            "crafting": {
                "name": "Crafting",
                "description": "Grab your rod and tackle! Come join your fellow anglers to go fishing!",
                "resources": []
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
            ]
        },
        'recipes': {
            'skill': 'cooking',
            'desserts': [
                cake
            ]
        },
        'plants': {
            'skill': 'gardening',
            'vegetables': [
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
