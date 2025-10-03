import random
from game.actions import *
from . import Fishing

class FishAction(Action):

    def __init__(self, species):
        self.species = species

    @property
    def requirements(self):
        return [
            LevelRequirement(
                skill=Fishing,
                level=self.fish.required_level
            ),
            ItemRequirement(
                item=self.bait,
                quantity=1
            )
        ]

    @property
    def rewards(self):
        return [
            ItemReward(
                item=self.fish,
                quantity=1
            ),
            ExperienceReward(
                skill=Fishing,
                quantity=self.fish.xp
            )
        ]

    def execute(self, player, bait):

        self.bait = bait

        drop_table = []
        for species in self.species:
            if player.experience.level(Fishing) < species.required_level:
                # Skip species if player lacks required level
                continue
            if not bait in species.required_bait:
                # Skip species if lacks required bait
                continue
            drop_table.append(species)

        # Gen a random fish from drop table
        self.fish = random.choice(drop_table)

        super().execute(player)
