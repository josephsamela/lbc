import random
from . import *

class FishAction(Action):

    def __init__(self, resources):
        self.skill = 'fishing'
        self.resources = resources

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

    def execute(self, game, player, target, quantity, *args, **kwargs):
        self.bait = game.items.get(target)
        self.quantity = int(quantity)

        drop_table = []
        for key,species in self.resources.items():
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
                'result': self.fish,
                'message': f'You caught a {self.fish.name.replace('Raw ', '')}!',
                'target': target,
                'quantity': self.quantity-1,
                'rewards': [
                    f'-1 {self.bait.name}',
                    f'+1 {self.fish.name}',
                    f'+{ self.fish.xp } Fishing Experience'
                ]
            }
        else:
            # Failure
            return {
                'result': self.fish,
                'message': f'You caught nothing.',
                'target': target,
                'quantity': self.quantity-1,
                'rewards':[
                    f'-1 {self.bait.name}',
                    f'0 Fishing Experience'
                ]
            }