from .skills import Skills
from .items import Items
from .locations import Locations

class Game:
    def __init__(self):
        self.skills = Skills()
        self.items = Items()
        self.locations = Locations()
