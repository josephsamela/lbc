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
        if self.player.journal.discovered(item):

            return InventorySlot(
                player=self.player, 
                item=item
            ).quantity

        else:
            return 0

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
        Add quantity of item to inventory
        '''
        InventorySlot(
            player=self.player,
            item=item
        ).quantity += quantity

    def remove(self, item, quantity):
        '''
        Remove quantity of item from inventory.
        '''
        if not self.check(item, quantity=quantity):
            raise Exception(f'Insuffient Item Quantity. Player {self.player.username} does not have {quantity} {item.name} to remove.')

        InventorySlot(
            player=self.player, 
            item=item
        ).quantity -= quantity

    def drop(self, item):
        '''
        Remove all quantity of item from inventory
        '''
        InventorySlot(
            player=self.player, 
            item=item
        ).quantity = 0

    def items(self):
        '''
        Return items in player inventory
        '''
        slots = []
        for slot in InventoryModel.select().where(
            (InventoryModel.player == self.player._record) &
            (InventoryModel.quantity > 0)
        ):
            slots.append(slot)

        return slots
