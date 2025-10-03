from game.actions import *
from . import Cooking

class CookItem(Action):

    @property
    def requirements(self):

        if not self.item.cookable:
            raise Exception(f'{self.item.name} cannot be cooked.')

        return [
            LevelRequirement(
                skill=Cooking,
                level=self.item.required_level
            ),
            ItemRequirement(
                item=self.item,
                quantity=1
            )
        ]

    @property
    def rewards(self):
        return [
            ItemReward(
                item=self.item.cooked,
                quantity=1
            ),
            ExperienceReward(
                skill=Cooking,
                quantity=self.item.xp
            )
        ]

    def execute(self, player, item):
        self.item = item
        super().execute(player)

class CookRecipe(Action):

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
                item=self.recipe,
                quantity=1
            ),
            ExperienceReward(
                skill=Cooking,
                quantity=self.recipe.xp
            )
        ]

    def execute(self, player, recipe):
        self.recipe = recipe
        super().execute(player)
