import random
from . import *
from common import flatten

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
            r.insert(0,
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

    def execute(self, game, player, target, quantity, attempt, *args, **kwargs):
        self.recipe = game.items.get(target)
        self.attempt = int(attempt)

        if not target in flatten(self.resources):
            raise Exception(f"You can't cook {self.recipe.name} here.")

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

        rewards = []
        for ingredient in self.recipe.ingredients:
            rewards.append(f'-1 {ingredient.name}')

        if result == 'Cooked':
            # Success
            rewards.append(f'+1 {self.recipe.name}')
            rewards.append(f'+{self.recipe.xp} Cooking Experience')
            return {
                'result': self.result,
                'resource': self.recipe.ingredients,
                'message': f'You made a {self.recipe.name}!',
                'target': target,
                'quantity': quantity,
                'attempt': self.attempt+1,
                'rewards': rewards
            }

        else:
            # Failure
            rewards.append(f'+1 {self.result.name}')
            rewards.append(f'{self.result.xp} Cooking Experience')
            return {
                'result': self.result,
                'resource': self.recipe.ingredients,
                'message': f'You made a {self.result.name}.',
                'target': target,
                'quantity': quantity,
                'attempt': self.attempt+1,
                'rewards': rewards
            }

