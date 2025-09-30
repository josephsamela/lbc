from . import *

from merchants.general import General
from merchants.tackle import Tackle

class GeneralStore(Location):
    name = 'General Store'
    merchant = General()

class TackleShop(Location):
    name = 'Bait & Tackle'
    merchant = Tackle()
