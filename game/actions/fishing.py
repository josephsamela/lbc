import random
from . import *

class FishAction(Action):

    def __init__(self, species):
        self.skill = 'fishing'
        self.species = species

    @property
    def requirements(self):
        if self.fish:
            return [
                LevelRequirement(
                    skill=self.skill,
                    level=self.fish.level
                ),
                ItemRequirement(
                    item=self.bait,
                    quantity=1
                )
            ]
        return []

    @property
    def rewards(self):
        if self.fish:
            return [
                ItemReward(
                    item=self.fish,
                    quantity=1
                ),
                ExperienceReward(
                    skill=self.skill,
                    quantity=self.fish.xp
                )
            ]
        return []

    def execute(self, game, player, bait, *args, **kwargs):
        self.bait = game.items.get(bait)

        drop_table = []
        for species in self.species:
            if player.experience.level(self.skill) < species.level:
                # Skip species if player lacks required level
                continue
            if not self.bait in species.bait:
                # Skip species if lacks required bait
                continue
            drop_table.append(species)

        # Gen a random fish from drop table
        self.fish = None
        if len(drop_table):
            self.fish = random.choice(drop_table)

        super().execute(player)

        if self.fish:
            # Success
            return {
                'item': self.fish,
                'message': f'You caught a {self.fish.name}!',
                'rewards': [
                    f'+{ self.fish.xp } Fishing Experience',
                    f'+1 {self.fish.name}'
                ]
            }
        else:
            # Failure
            return {
                'item': self.fish,
                'message': f'You caught nothing.',
                'rewards':[
                    f'+0 Fishing Experience'
                ]
            }