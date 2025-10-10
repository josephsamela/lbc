from .actions.fishing import FishAction
from .actions.cooking import CookAction
from .actions.crafting import CraftAction

from .items import *

class Game:
    def __init__(self):
        self.skills = {
            "fishing": {
                "name": "Fishing",
                "resources": [
                    raw_pink_salmon,
                    raw_coho_salmon,
                    raw_sockeye_salmon,
                    raw_chinook_salmon
                ]
            }
        }

        self.locations = {
            "tributary_river": {
                "actions": [
                    FishAction([
                        raw_pink_salmon,
                        raw_coho_salmon,
                        raw_sockeye_salmon,
                        raw_chinook_salmon
                    ])
                ]
            },
            "cozy_campfire": {
                "actions": [
                    CookAction()
                ]
            },
            "craft_pavilion": {
                "actions": [
                    CraftAction()
                ]
            }
        }

    journal = {
        'fish': {
            'salmon': [
                raw_pink_salmon,
                raw_coho_salmon,
                raw_sockeye_salmon,
                raw_chinook_salmon
            ]
        },
        'recipes': {
            'desserts': [
                cake
            ]
        },
        'bait': {
            'lures': [
                crankbait
            ],
            'flies': [
                pheasant_tail
            ]
        }
    }
