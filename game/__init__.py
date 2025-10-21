from .actions.fishing import FishAction
from .actions.crafting import CraftAction
from .actions.cooking import CookAction
from .actions.shopping import BuyAction, SellAction

from .items.fish import fish, lake, river, ocean, coral_reef
from .items.bait import bait
from .items.crafting_recipes import crafting_recipes, flies, lures, materials, nymphs, wet_flies, dry_flies, streamers
from .items.cooking_recipes import cooking_recipes, cooked_fish, campfire_recipes

from common import flatten

class Game:
    def __init__(self):

        self.locations = {
            "market": {     
                "name": "Market",
                "description": "The market is a fun place where folks gather to buy and sell items with Lute Bear Coin!",
                "bait_store": {
                    "name": "Bait Store",
                    "description": "The corner bait store that specializes in vermiculture and selling live bait!",
                    "action": BuyAction(resources=bait)
                },
                "tackle_shop": {
                    "name": "Tackle Shop",
                    "description": "The local tackle shop that sells materials for crafting lures and tying flies!",
                    "action": BuyAction(resources=materials)
                },
                "flea_market": {
                    "name": "Flea Market",
                    "description": "The community market where you can sell any item in your inventory!",
                    "action": SellAction()
                }
            },
            "fishing": {
                "name": "Fishing",
                "description": "Explore lakes, rivers and oceans to fish exciting locations and discover new species!",
                "lake": {
                    "name": "Lake",
                    "description": "A cold and switch freshwater river that's home to many species!",
                    "resource_filter": ["live", "lures", "nymphs", "wet flies", "dry flies", "streamers"],
                    "action": FishAction(resources=lake)
                },
                "river": {
                    "name": "River",
                    "description": "A cold and switch freshwater river that's home to many species!",
                    "resource_filter": ["live", "lures", "nymphs", "wet flies", "dry flies", "streamers"],
                    "action": FishAction(resources=river)
                },
                "ocean": {
                    "name": "Ocean",
                    "description": "A cold and switch freshwater river that's home to many species!",
                    "resource_filter": ["live", "lures", "nymphs", "wet flies", "dry flies", "streamers"],
                    "action": FishAction(resources=ocean)
                },
                "coral reef": {
                    "name": "Coral Reef",
                    "description": "A cold and switch freshwater river that's home to many species!",
                    "resource_filter": ["live", "lures", "nymphs", "wet flies", "dry flies", "streamers"],
                    "action": FishAction(resources=coral_reef)
                }
            },
            "crafting": {
                "name": "Crafting",
                "description": "Gather materials and use your creativity to craft lures and flies for fishing!",
                "lakeside cottage": {
                    "name": "Lakeside Cottage",
                    "description": "A charming cottage by the lake with a workshop and tools for crafting lures.",
                    "action": CraftAction(resources={'lures': lures})
                },
                "river lodge": {
                    "name": "River Lodge",
                    "description": "Rustic lodge overlooking the river with good light and a fly tying stand for crafting flies.",
                    "action": CraftAction(resources=flies)
                }
            },
            "cooking": {
                "name": "Cooking",
                "description": "Combine the ingredients you've collected to discover recipes and cook delicious meals!",
                "campfire": {
                    "name": "Campfire",
                    "description": "A cozy fire by with a warm bed of coals - perfect for cooking your catch.",
                    "action": CookAction(resources=campfire_recipes)
                }
            }
        }

        self.skills = {
            "fishing": {
                "name": "Fishing",
                "description": "Explore lakes, rivers and oceans to fish exciting locations and discover new species!"
            },
            "crafting": {
                "name": "Crafting",
                "description": "Gather materials and combine them to craft lures and flies for fishing!"
            },
            "cooking": {
                "name": "Cooking",
                "description": "Use the ingredients you've collected to cook unique and exciting recipes!"
            }
        }

        self.journal = {
            'fishing': {
                'skill': 'fishing',
                'lake': lake,
                'river': river,
                'ocean': ocean,
                'coral reef': coral_reef
            },
            'crafting': {
                'skill': 'crafting',
                'lures': lures,
                'nymphs': nymphs,
                'dry flies': dry_flies,
                'wet flies': wet_flies,
                'streamers': streamers
            },
            'cooking': {
                'skill': 'cooking',
                'fish': cooked_fish
            }
        }

        # Build LUT of every item
        self.items = {}
        for group in [fish, bait, crafting_recipes, materials, cooking_recipes]:
            self.items.update(flatten(group))

        # Attach skill & location info to items
        from app import snake_case
        for skill, locations in self.locations.items():
            for location_key,location in locations.items():

                if isinstance(location, str):
                    continue

                for item_key, item in flatten(location['action'].resources).items():
                
                    item.skill = skill
                    item.location = location
                    item.location_key = location_key

                    if hasattr(item, 'burnt'):
                        self.items[ snake_case(item.burnt.name) ] = item.burnt

    @staticmethod
    def by_level(items):
        '''
        Take a nested dict of items and flatten to list.
        Sort list by "level" requirement of the items ASC.
        '''
        i = {}

        for chapter, contents in items.items():
            if isinstance(contents, dict):
                i.update(contents)

        # Sort by level ascending
        return dict(sorted(i.items(), key=lambda x: x[1].level))
