import datetime
from . import *

class PlantAction(Action):

    def __init__(self, resources):
        self.resources = resources

    '''
    Plant seed in garden.
    '''
    @property
    def requirements(self):
        '''
        Player needs required recipe level and ingredients
        '''
        r = [
            LevelRequirement(
                skill=Gardening,
                level=self.seed.required_level
            ),
            ItemRequirement(
                item=self.seed,
                quantity=1
            )
        ]
        return r

    def execute(self, player, garden, seed):

        # Check that garden doesn't already have something planted there!
        self.garden = garden(player=player)
        if self.garden.seed:
            raise Exception('Garden already planted.')

        # Check plant requirements
        self.seed = seed
        super().execute(player)

        # Update garden with new seed
        self.garden.seed = seed
        self.garden.plant = seed
        self.garden.planted_at = datetime.datetime.now()

        return garden

class HarvestAction(Action):
    '''
    Harvest plant from garden.
    '''
    @property
    def rewards(self):
        return [
            ItemReward(
                item=self.plant,
                quantity=1
            ),
            ExperienceReward(
                skill=Gardening,
                quantity=self.plant.xp
            )
        ]

    def execute(self, player, garden):

        # Check something is planted here!
        self.garden = garden(player=player)
        if not self.garden.seed:
            raise Exception('Garden has nothing planted.')

        # Clear plant from garden
        self.plant = self.garden.plant.fruit()
        self.garden.seed = None
        self.garden.planted_at = None

        # Reward player
        super().execute(player)
        return self.plant

class ClearAction(Action):
    '''
    Clear plant from garden.
    '''
    def execute(self, player, garden):

        # Check something is planted here!
        self.garden = garden(player=player)
        if not self.garden.seed:
            raise Exception('Garden has nothing planted.')

        # Clear plant from garden
        self.garden.seed = None
        self.garden.planted_at = None

        super().execute(player)
