from db import Record, ItemModel

class Item(Record):
    _model = ItemModel

from .bait import Baits
from .lures import Lures

class Items:
    bait = Baits()
    lures = Lures()
