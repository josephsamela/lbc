from . import *

class DropAction(Action):

    @property
    def requirements(self):
        '''
        Check player inventory has item quantity
        '''
        return [
            ItemRequirement(
                item=self.item,
                quantity=self.quantity
            )
        ]

    @property
    def rewards(self):
        '''
        Remove item quantity from player inventory
        '''
        return [
            ItemReward(
                item=self.item,
                quantity= -self.quantity # Add negative (-) item quantity
            )
        ]

    def execute(self, player, item, quantity):
        self.item = item
        self.quantity = quantity
        super().execute(player)
