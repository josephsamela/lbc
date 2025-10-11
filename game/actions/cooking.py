import random
from . import *

class CookAction(Action):

    def __init__(self):
        self.skill = 'Cooking'

    @property
    def requirements(self):
        '''
        Player needs required recipe level and ingredients
        '''
        r = [
            LevelRequirement(
                skill=self.skill,
                level=self.recipe.level
            )
        ]
        for ingredient in self.recipe.ingredients:
            r.append(
                ItemRequirement(
                    item=ingredient,
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
                skill=self.skill,
                quantity=self.result.xp
            )
        ]

    def execute(self, player, recipe):

        self.recipe = recipe

        # Cooking success or failure is random. However, the outcome
        # is weighted by recipe difficulty and player skill.
        options = ['Cooked', 'Burnt']
        weights = [player.experience.level(self.skill) , self.recipe.xp/10 ]
        result = random.choices(options, weights=weights)[0]

        match result:
            case 'Cooked':
                self.result = self.recipe
            case 'Burnt':
                self.result = self.recipe.burnt
                # self.result.name.replace('Cooked ','')
                c = 0 # Burnt food rewards zero xp

        super().execute(player)
        return self.result
