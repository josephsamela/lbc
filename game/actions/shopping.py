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
                quantity=self.total_cost
            )
        ]

    @property
    def rewards(self):
        return [
            ItemReward(
                item=self.item,
                quantity=self.quantity 
            ),
            BalanceReward(
                quantity= -(self.total_cost)
            )
        ]

    def execute(self, game, player, target, quantity, *args, **kwargs):
        self.item = game.items.get(target)
        self.quantity = int(quantity)
        self.total_cost = self.item.cost * self.quantity

        if not target in flatten(self.resources):
            raise Exception(f'{self.item.name} is not for sale.')

        super().execute(player)

        return {
            'result': self.item,
            'message': f'You purchased {self.quantity} {self.item.name} for {self.total_cost} LBC!',
            'target': target,
            'rewards': [
                f'+{self.quantity} {self.item.name}',
                f'-{ self.total_cost } LBC'
            ]
        }

class SellAction(Action):

    def __init__(self):
        self.resources = {}

    @property
    def requirements(self):
        return [
            ItemRequirement(
                item=self.item,
                quantity=self.quantity
            )
        ]

    @property
    def rewards(self):
        return [
            ItemReward(
                item=self.item,
                quantity=-(self.quantity)
            ),
            BalanceReward(
                quantity=self.total_cost
            )
        ]

    def execute(self, game, player, target, quantity, *args, **kwargs):
        self.item = game.items.get(target)
        self.quantity = int(quantity)
        self.total_cost = self.item.cost * self.quantity

        super().execute(player)

        return {
            'result': self.item,
            'message': f'You sold {self.quantity} {self.item.name} for {self.total_cost} LBC!',
            'target': target,
            'rewards': [
                f'+{self.quantity} {self.item.name}',
                f'-{ self.total_cost } LBC'
            ]
        }
