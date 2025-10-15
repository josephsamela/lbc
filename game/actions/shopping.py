from . import *
from common import flatten

class BuyAction(Action):

    def __init__(self, resources):
        # Dict of items for sale
        self.resources = resources

    @property
    def requirements(self):
        return [
            BalanceRequirement(
                quantity=self.item.cost
            )
        ]

    @property
    def rewards(self):
        return [
            ItemReward(
                item=self.item,
                quantity=1 # Only support buying items one at a time atm
            ),
            BalanceReward(
                quantity= -self.item.cost # Subtract item cost from player balance
            )
        ]

    def execute(self, game, player, target, *args, **kwargs):
        self.item = game.items.get(target)

        if not target in flatten(self.resources):
            raise Exception(f'{self.item.name} is not for sale.')

        super().execute(player)

        return {
            'result': self.item,
            'message': f'You purchased {self.item.name} for {self.item.cost} LBC!',
            'target': self.item,
            'repeat_text': 'Buy Again',
            'rewards': [
                f'+1 {self.item.name}',
                f'-{ self.item.cost } LBC'
            ]
        }
