from db import InventoryModel
from game import flatten

class JournalManager:
    def __init__(self, player):
        self.player = player

    def discovered_item(self, item):
        '''
        Check if player has discovered an item
        '''
        return InventoryModel.select().where(
            (InventoryModel.player == self.player._record) & 
            (InventoryModel.item == item._record)
        ).exists()

    def discover(self, item):
        '''
        Discover an item
        '''
        self.player.inventory.add(item, quantity=0)

    def discoverable(self, chapter):
        '''
        Return count of discoverable items in chapter
        '''
        return len(flatten(chapter))
    
    def discovered(self, chapter):
        '''
        Return count of discovered items in chapter
        '''
        c = 0
        for _,item in flatten(chapter).items():
            if self.discovered_item(item):
                c += 1
        return c
    
    def progress(self, chapter):
        '''
        Return chapter progress as decimal
        '''
        return round((self.discovered(chapter)/self.discoverable(chapter))*100)
