import re

class Location:
    description = '' # Location paragraph description
    locations = []   # List of sub-locations accessible from this location
    actions = []     # List of actions that can be performed here
    resources = []   # List of resources that can be gathered here

    action_text = '' # Text to display on action button

    @property
    def name(self):
        '''
        Return name of object class.

        Add space " " between words. "PinkSalmon" -> "Pink Salmon".
        '''
        pattern=r'([a-z](?=[A-Z])|[A-Z](?=[A-Z][a-z]))'
        replace=r'\1 '
        name=self.__class__.__name__
        return re.sub(pattern, replace, name)

    @property
    def icon(self):
        return self.name.lower().replace(' ', '_')+'.png'

from game.skills.fishing.actions import FishAction
class FishingLocation(Location):

    fish = [] # Fish that can be caught at this location
    actions = [FishAction]
    action_text = 'Fishing'

    @property
    def resources(self):
        return self.fish

from game.skills.cooking.actions import CookAction
class CookingLocation(Location):

    recipes = [] # Recipes that can be cooked at this location
    actions = [CookAction]
    action_text = 'Cooking'

    @property
    def resources(self):
        return self.recipes

from game.skills.crafting.actions import CraftAction
class CraftingLocation(Location):

    recipes = [] # Items that can be crafted at this location
    actions = [CraftAction]
    action_text = 'Crafting'

    @property
    def resources(self):
        return self.recipes

from game.skills.gardening.actions import PlantAction, HarvestAction, ClearAction
class GardeningLocation(Location):

    plants = [] # Plants that can be grown at this location
    actions = [PlantAction, HarvestAction, ClearAction]
    action_text = 'Gardening'

    @property
    def resources(self):
        return self.plants
