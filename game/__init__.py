from .actions.fishing import FishAction
from .actions.crafting import CraftAction
from .actions.cooking import CookAction

from .items.fish import fish
from .items.bait import bait
from .items.crafting_recipes import crafting_recipes
from .items.cooking_recipes import cooking_recipes

class Game:
    def __init__(self):

        self.items = self.flatten([fish, bait, crafting_recipes, cooking_recipes])

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
                    "action": FishAction(resources=fish['lake'].values())
                },
                "river": {
                    "name": "River",
                    "description": "A cold and switch freshwater river that's home to many species!",
                    "action_disabled_text": "Select Bait",
                    "action_enabled_text": "Fish",
                    "input": "inventory", # Either "inventory" or "resources"
                    "resource_subtitle": "Choose bait from your inventory!",
                    "resource_filter": ["live", "lures", "nymphs", "wet flies", "dry_files", "streamers"],
                    "action": FishAction(resources=fish['river'].values())
                },
                "ocean": {
                    "name": "Ocean",
                    "description": "A cold and switch freshwater river that's home to many species!",
                    "action_disabled_text": "Select Bait",
                    "action_enabled_text": "Fish",
                    "input": "inventory", # Either "inventory" or "resources"
                    "resource_subtitle": "Choose bait from your inventory!",
                    "resource_filter": ["live", "lures", "nymphs", "wet flies", "dry_files", "streamers"],
                    "action": FishAction(resources=fish['ocean'].values())
                },
                "coral reef": {
                    "name": "Coral Reef",
                    "description": "A cold and switch freshwater river that's home to many species!",
                    "action_disabled_text": "Select Bait",
                    "action_enabled_text": "Fish",
                    "input": "inventory", # Either "inventory" or "resources"
                    "resource_subtitle": "Choose bait from your inventory!",
                    "resource_filter": ["live", "lures", "nymphs", "wet flies", "dry_files", "streamers"],
                    "action": FishAction(resources=fish['coral reef'].values())
                }
            },
            "crafting": {
                "pavilion": {
                    "name": "Pavilion",
                    "description": "A cold and switch freshwater river that's home to many species!",
                    "action_disabled_text": "Select Recipe",
                    "action_enabled_text": "Craft",
                    "input": "resources", # Either "inventory" or "resources"
                    "resource_subtitle": "Choose an item to craft!",
                    "resource_filter": ["lures"],
                    "action": CraftAction(resources=crafting_recipes['lures'].values())
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
                    "resource_filter": ["lures"],
                    "action": CookAction(resources=cooking_recipes['fish'].values())
                }
            }
        }

        self.skills = {
            "fishing": {
                "name": "Fishing",
                "description": "Explore lakes, rivers and oceans to fish exciting locations and discover new species!",
                "resources": self.by_level(fish)
            },
            "crafting": {
                "name": "Crafting",
                "description": "Explore lakes, rivers and oceans to fish exciting locations and discover new species!",
                "resources": self.by_level(crafting_recipes)
            },
            "cooking": {
                "name": "Cooking",
                "description": "Explore lakes, rivers and oceans to fish exciting locations and discover new species!",
                "resources": self.by_level(cooking_recipes)
            }
        }

        self.journal = {
            'Fish': fish,
            'Bait': crafting_recipes,
            'Food': cooking_recipes
        }

    @staticmethod
    def flatten(item_groups):
        '''
        Take list of item groups (dict) and flatten into a one-layer dict
        '''
        i = {}
        for item_group in item_groups:
            for _,group in item_group.items():
                if isinstance(group, dict):
                    i.update(group)
        return i

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
