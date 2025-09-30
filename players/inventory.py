from . import *

from items import ItemModel
class InventorySlotModel(Base):
    class Meta:
        db_table = 'inventories'
    player = ForeignKeyField(PlayerModel)
    item = ForeignKeyField(ItemModel)
    quantity = IntegerField(default=0)

class InventorySlot(Record):
    _model = InventorySlotModel
    # def __init__(self, player, item):
    #     record, created = self._model.get_or_create(
    #         player=player._record,
    #         item=item._record
    #     )
    #     self.player = record.player
    #     self.item = record.item
    #     self.quantity = record.quantity

class Inventory:
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
