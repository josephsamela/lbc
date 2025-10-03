from db import Record, PlayerModel

from .inventory import InventoryManager
from .experience import ExperienceManager
from .journal import JournalManager

class Player(Record):
    _model = PlayerModel

    def __init__(self):
        self.inventory = InventoryManager(self)
        self.experience = ExperienceManager(self)
        self.journal = JournalManager(self)
