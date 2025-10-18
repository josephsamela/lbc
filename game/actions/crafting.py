from . import *
from common import flatten

class CraftAction(Action):

    def __init__(self, resources):
        self.skill = 'crafting'
        self.resources = resources

    @property
    def requirements(self):
        '''
        Player needs required recipe level and materials
        '''
        r = [
            LevelRequirement(
                skill=self.skill,
                level=self.recipe.level
            )
        ]
        for material in self.recipe.materials:
            r.append(
                ItemRequirement(
                    item=material,
                    quantity=1
                )
            )
        return r

    @property
    def rewards(self):
        '''
        Player receives finished recipe and experience
        '''
        return [
            ItemReward(
                item=self.recipe,
                quantity=1
            ),
            ExperienceReward(
                skill=self.skill,
                quantity=self.recipe.xp
            )
        ]

    def execute(self, game, player, target, quantity, attempt, *args, **kwargs):
        self.recipe = game.items.get(target)
        self.attempt = int(attempt)

        if not target in flatten(self.resources):
            raise Exception(f"You can't craft {self.recipe.name} here.")

        super().execute(player)

        rewards = []
        for material in self.recipe.materials:
            rewards.append(f'-1 {material.name}')
        rewards.append(f'+1 {self.recipe.name}')
        rewards.append(f'+{self.recipe.xp} Crafting Experience')

        return {
            'result': self.recipe,
            'resource': self.recipe.materials,
            'message': f'You crafted a {self.recipe.name}!',
            'target': target,
            'quantity': quantity,
            'attempt': self.attempt+1,
            'rewards': rewards
        }
