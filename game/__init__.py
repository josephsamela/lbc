from .actions.fishing import FishAction
from .actions.crafting import CraftAction
from .actions.cooking import CookAction

from .items.fish import fish, lake, river, ocean, coral_reef
from .items.bait import bait
from .items.crafting_recipes import crafting_recipes, flies, lures
from .items.cooking_recipes import cooking_recipes, cooked_fish

@staticmethod
def flatten(d, parent='', level=0):
    items = {}

    for k, v in d.items():
        
        if isinstance(v, str):
            continue

        if isinstance(v, dict):
            level+=1
            items.update(flatten(v, k, level))
        else:
            v.key = k
            v.chapter = parent
            items[k] = v

    return items


class Game:
    def __init__(self):

        self.locations = {
            "fishing": {
                "lake": {
                    "name": "Lake",
                    "description": "A cold and switch freshwater river that's home to many species!",
                    "action_disabled_text": "Select Bait",
                    "action_enabled_text": "Fish",
                    "input": "inventory", # Either "inventory" or "resources"
                    "resource_subtitle": "Choose bait from your inventory!",
                    "resource_filter": ["live", "lures", "nymphs", "wet flies", "dry_files", "streamers"],
                    "action": FishAction(resources=lake)
                },
                "river": {
                    "name": "River",
                    "description": "A cold and switch freshwater river that's home to many species!",
                    "action_disabled_text": "Select Bait",
                    "action_enabled_text": "Fish",
                    "input": "inventory", # Either "inventory" or "resources"
                    "resource_subtitle": "Choose bait from your inventory!",
                    "resource_filter": ["live", "lures", "nymphs", "wet flies", "dry_files", "streamers"],
                    "action": FishAction(resources=river)
                },
                "ocean": {
                    "name": "Ocean",
                    "description": "A cold and switch freshwater river that's home to many species!",
                    "action_disabled_text": "Select Bait",
                    "action_enabled_text": "Fish",
                    "input": "inventory", # Either "inventory" or "resources"
                    "resource_subtitle": "Choose bait from your inventory!",
                    "resource_filter": ["live", "lures", "nymphs", "wet flies", "dry_files", "streamers"],
                    "action": FishAction(resources=ocean)
                },
                "coral reef": {
                    "name": "Coral Reef",
                    "description": "A cold and switch freshwater river that's home to many species!",
                    "action_disabled_text": "Select Bait",
                    "action_enabled_text": "Fish",
                    "input": "inventory", # Either "inventory" or "resources"
                    "resource_subtitle": "Choose bait from your inventory!",
                    "resource_filter": ["live", "lures", "nymphs", "wet flies", "dry_files", "streamers"],
                    "action": FishAction(resources=coral_reef)
                }
            },
            "crafting": {
                "lakeside_cottage": {
                    "name": "Lakeside Cottage",
                    "description": "A charming cottage by the lake with a workshop and tools for crafting lures.",
                    "action_disabled_text": "Select Recipe",
                    "action_enabled_text": "Craft",
                    "input": "resources", # Either "inventory" or "resources"
                    "resource_subtitle": "Choose an lure to craft!",
                    "resource_filter": ["lures"],
                    "action": CraftAction(resources=lures)
                },
                "river_lodge": {
                    "name": "River Lodge",
                    "description": "Rustic lodge overlooking the river with good light and a fly tying stand for crafting flies.",
                    "action_disabled_text": "Select Recipe",
                    "action_enabled_text": "Craft",
                    "input": "resources", # Either "inventory" or "resources"
                    "resource_subtitle": "Choose a fly to craft!",
                    "resource_filter": ["lures"],
                    "action": CraftAction(resources=flies)
                }
            },
            "cooking": {
                "campfire": {
                    "name": "Campfire",
                    "description": "A cold and switch freshwater river that's home to many species!",
                    "action_disabled_text": "Select Recipe",
                    "action_enabled_text": "Cook",
                    "input": "resources", # Either "inventory" or "resources"
                    "resource_subtitle": "Choose an recipe to cook!",
                    "action": CookAction(resources=cooked_fish)
                }
            }
        }

        self.skills = {
            "fishing": {
                "name": "Fishing",
                "description": "Explore lakes, rivers and oceans to fish exciting locations and discover new species!",
            },
            "crafting": {
                "name": "Crafting",
                "description": "Explore lakes, rivers and oceans to fish exciting locations and discover new species!",
            },
            "cooking": {
                "name": "Cooking",
                "description": "Explore lakes, rivers and oceans to fish exciting locations and discover new species!",
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
                'nymphs': flies['nymphs'],
                'dry flies': flies['dry flies'],
                'wet flies': flies['wet flies'],
                'streamers': flies['streamers']
            },
            'cooking': {
                'skill': 'cooking',
                'fish': cooked_fish
            }
        }

        # Build LUT of every item
        self.items = {}
        for group in [fish, bait, crafting_recipes, cooking_recipes]:
            self.items.update(flatten(group))

        # Attach skill & location info to items
        for skill, locations in self.locations.items():
            for location_key,location in locations.items():
                for item_key, item in flatten(location['action'].resources).items():
                
                    item.skill = skill
                    item.location = location
                    item.location_key = location_key

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
