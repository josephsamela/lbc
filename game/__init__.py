from .actions.fishing import FishAction

from .items.fish import fish
from .items.bait import bait
from .items.crafting_recipes import crafting_recipes

class Game:
    def __init__(self):

        self.items = self.flatten([fish, bait, crafting_recipes])

        self.locations = {
            "fishing": {
                "tributary_river": {
                    "name": "Tributary River",
                    "description": "A cold and switch freshwater river that's home to many species!",
                    "action_text": "Go Fishing",
                    "action": FishAction(
                            species=fish['lakes'].values()
                        )
                },
                "estuary": {
                    "name": "Estuary",
                    "description": "The Estuary is a coastal brakish environment that's home to many diverse species of fish!",
                    "actions": []
                },
                "open_ocean": {
                    "name": "Open Ocean",
                    "description": "The Open Ocean is a rough saltwater marine environment with many species of large fish!",
                    "actions": []
                },
                "coral_reef": {
                    "name": "Coral Reef",
                    "description": "The Coral Reef is a vibrant warmwater marine ecosystem with many colorful fish!",
                    "actions": []
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
            }
        }

        self.journal = {
            'Fish': fish,
            'Bait': crafting_recipes
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
