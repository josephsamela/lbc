from .actions.fishing import FishAction
from .actions.cooking import CookAction
from .actions.crafting import CraftAction

from .items import *

class Game:
    def __init__(self):


        self.items = {}
        for name in dir(items):
            i = getattr(items, name)
            if isinstance(i, Item):
                self.items[name] = i

        self.skills = {
            "fishing": {
                "name": "Fishing",
                "description": "Explore lakes, rivers and oceans to fish exciting locations and discover new species!",
                "resources": [
                    raw_bluegill,
                    raw_brown_trout,
                    raw_scup,
                    raw_sergeant_major,
                    raw_pumpkinseed,
                    raw_brook_trout,
                    raw_menhaden,
                    raw_yellowtail_snapper,
                    raw_yellow_perch,
                    raw_rainbow_trout,
                    raw_striped_bass,
                    raw_spanish_mackerel,
                    raw_smallmouth_bass,
                    raw_channel_catfish,
                    raw_searobin,
                    raw_goatfish,
                    raw_walleye,
                    raw_pink_salmon,
                    raw_black_seabass,
                    raw_parrotfish,
                    raw_largemouth_bass,
                    raw_chum_salmon,
                    raw_arctic_cod,
                    raw_chain_pickerel,
                    raw_coho_salmon,
                    raw_bluefish,
                    raw_hogfish,
                    raw_muskellunge,
                    raw_longnose_gar,
                    raw_pacific_halibut,
                    raw_red_grouper,
                    raw_mahi_mahi,
                    raw_northern_pike,
                    raw_sockeye_salmon,
                    raw_bluefin_tuna,
                    raw_giant_trevally,
                    raw_lake_sturgeon,
                    raw_chinook_salmon,
                    raw_swordfish,
                    raw_humphead_wrasse
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

        self.journal = {
            'fish': {
                'skill': 'fishing',
                'Lakes': [
                    raw_bluegill,
                    raw_pumpkinseed,
                    raw_yellow_perch,
                    raw_smallmouth_bass,
                    raw_walleye,
                    raw_largemouth_bass,
                    raw_chain_pickerel,
                    raw_muskellunge,
                    raw_northern_pike,
                    raw_lake_sturgeon
                ],
                'Rivers': [
                    raw_brown_trout,
                    raw_brook_trout,
                    raw_rainbow_trout,
                    raw_channel_catfish,
                    raw_pink_salmon,
                    raw_chum_salmon,
                    raw_coho_salmon,
                    raw_longnose_gar,
                    raw_sockeye_salmon,
                    raw_chinook_salmon
                ],
                'Ocean': [
                    raw_scup,
                    raw_menhaden,
                    raw_striped_bass,
                    raw_searobin,
                    raw_black_seabass,
                    raw_arctic_cod,
                    raw_bluefish,
                    raw_pacific_halibut,
                    raw_bluefin_tuna,
                    raw_swordfish
                ],
                'Coral Reef': [
                    raw_sergeant_major,
                    raw_yellowtail_snapper,
                    raw_spanish_mackerel,
                    raw_goatfish,
                    raw_parrotfish,
                    raw_hogfish,
                    raw_mahi_mahi,
                    raw_red_grouper,
                    raw_giant_trevally,
                    raw_humphead_wrasse
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


