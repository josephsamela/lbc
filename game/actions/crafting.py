from . import *

class CraftAction(Action):

    def __init__(self):
        self.skill = 'Crafting'

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

    def execute(self, player, recipe):
        self.recipe = recipe

        super().execute(player)
        return self.recipe
