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

        if not target in self.resources:
            raise Exception(f"You can't craft {self.recipe.name} here.")

        super().execute(player)

        return {
            'result': self.recipe,
            'message': f'You crafted a {self.recipe.name}!',
            'target': self.recipe,
            'repeat_text': 'Craft Again',
            'rewards': [
                f'+1 {self.recipe.name}',
                f'+{ self.recipe.xp } Crafting Experience'
            ]
        }
