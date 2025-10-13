from . import *

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

    def execute(self, game, player, target, *args, **kwargs):
        self.recipe = game.items.get(target)

        if not self.recipe in self.resources:
            raise Exception(f"You can't craft {recipe.name} here.")

        super().execute(player)

        return {
            'item': self.recipe,
            'message': f'You crafted a {self.recipe.name}!',
            'param': self.recipe,
            'repeat_text': 'Craft Again',
            'rewards': [
                f'+1 {self.recipe.name}',
                f'+{ self.recipe.xp } Crafting Experience'
            ]
        }
