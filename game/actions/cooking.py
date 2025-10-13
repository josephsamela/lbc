import random
from . import *

class CookAction(Action):

    def __init__(self, resources):
        self.skill = 'cooking'
        self.resources = resources

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

    def execute(self, game, player, target, *args, **kwargs):
        self.recipe = game.items.get(target)

        if not self.recipe in self.resources:
            raise Exception(f"You can't cook {recipe.name} here.")

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
        
        if result == 'Cooked':
            # Success
            return {
                'item': self.result,
                'message': f'You made {self.result.name}!',
                'param': self.recipe,
                'repeat_text': 'Cook Again',
                'rewards': [
                    f'+1 {self.result.name}',
                    f'+{ self.recipe.xp } Cooking Experience'
                ]
            }
        else:
            # Failure
            return {
                'item': self.result,
                'message': f'You made a {self.result.name}.',
                'param': self.recipe,
                'repeat_text': 'Cook Again',
                'rewards':[
                    f'+1 {self.result.name}',
                    f'+0 Cooking Experience'
                ]
            }

