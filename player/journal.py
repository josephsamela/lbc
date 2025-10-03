from db import InventoryModel

class JournalManager:
    def __init__(self, player):
        self.player = player

    def discovered(self, item):
        '''
        Check if player has discovered an item
        '''
        return InventoryModel.select().where(
            (InventoryModel.player == self.player.id) & 
            (InventoryModel.item == item.id)
        ).exists()

    def discover(self, item):
        '''
        Discover an item
        '''
        self.player.inventory.add(item, quantity=0)
