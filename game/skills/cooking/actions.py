import random

from game.actions import *
from . import Cooking

class CookAction(Action):

    @property
    def requirements(self):
        '''
        Player needs required recipe level and ingredients
        '''
        r = [
            LevelRequirement(
                skill=Cooking,
                level=self.recipe.required_level
            )
        ]
        for ingredient in self.recipe.ingredients:
            r.append(
                ItemRequirement(
                    item=ingredient(),
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
                item=self.result,
                quantity=1
            ),
            ExperienceReward(
                skill=Cooking,
                quantity=self.result.xp
            )
        ]

    def execute(self, player, item=None, recipe=None):

        if not item and not recipe:
            raise Exception('You must pass item or recipe.')

        elif item:
            if not item.cookable:
                raise Exception(f'{item.name} cannot be cooked.')
            item.ingredients = [item.__class__]
            self.recipe = item

        elif recipe:
            self.recipe = recipe

        # Cooking success or failure is random. However, the outcome
        # is weighted by recipe difficulty and player skill.
        options = [self.recipe.cooked(), self.recipe.burnt()]
        weights = [player.experience.level(Cooking) , self.recipe.xp/10 ]
        self.result = random.choices(options, weights=weights)[0]

        # Burnt food rewards zero xp
        if self.result.state == 'Burnt':
            self.result.xp = 0

        super().execute(player)
        return self.result
