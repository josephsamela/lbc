from db import InventoryModel, ItemModel, fn

class InventoryManager:
    def __init__(self, player):
        self.player = player

    def count_all(self):
        '''
        Sum of quantity of all items in inventory
        '''
        r = InventoryModel.select(
            fn.SUM(InventoryModel.quantity)
        ).where(
            InventoryModel.player==self.player._record
        ).scalar()

        if r:
            return r
        return 0

    def count(self, item):
        '''
        Count quantity of item in inventory
        '''
        if self.player.journal.discovered_item(item):
            return InventoryModel.get(
                player=self.player._record, 
                item=item._record
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
        r,c = InventoryModel.get_or_create(
            player=self.player._record,
            item=item._record
        )
        r.quantity += quantity
        r.save()

    def remove(self, item, quantity):
        '''
        Remove quantity of item from inventory.
        '''
        if not self.check(item, quantity=quantity):
            raise Exception(f'Insuffient Item Quantity. Player {self.player.username} does not have {quantity} {item.name} to remove.')

        r = InventoryModel.get(
            player=self.player._record, 
            item=item._record
        )
        r.quantity -= quantity
        r.save()

    def drop(self, item):
        '''
        Remove all quantity of item from inventory
        '''
        if self.count(item) == 0:
            return
        r = InventoryModel.get(
            player=self.player._record, 
            item=item._record
        )
        r.quantity = 0
        r.save()

    def items(self, filter=None):
        '''
        Return items in player inventory
        Optional. Filter items by category. For example filter='bait' only return bait items.
        '''
        if not filter:
            filter = [ItemModel.category]

        slots = []
        for slot in InventoryModel.select().join(ItemModel).where(
            (InventoryModel.item == ItemModel.id) &
            (InventoryModel.player == self.player._record) &
            (InventoryModel.quantity > 0) &
            (ItemModel.category << filter)
        ):
            slots.append(slot)

        return slots
