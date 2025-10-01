from db import Record, InventoryModel

class InventorySlot(Record):
    _model = InventoryModel

class InventoryManager:
    def __init__(self, player):
        self.player = player

    def count(self, item):
        '''
        Count quantity of item in inventory
        '''
        return InventorySlot(
            player=self.player, 
            item=item
        ).quantity

    def check(self, item, quantity=1):
        '''
        Check if quantity of item exists in inventory
        '''
        if self.count(item) >= quantity:
            return True
        else:
            return False

    def add(self, item, quantity=1):
        '''
        Add quantity of items to inventory
        '''
        InventorySlot(
            player=self.player, 
            item=self.player
        ).quantity += quantity

    def remove(self, item, quantity=1):
        '''
        Remove quantity of items from inventory.
        '''
        if not self.check(item, quantity=quantity):
            raise Exception(f'Insuffient Item Quantity. Player {self.player.username} does not have {quantity} {item.name} to remove.')

        InventorySlot(
            player=self.player, 
            item=item
        ).quantity -= quantity
