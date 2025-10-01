from db import Record, LocationModel

class Location(Record):
    _model = LocationModel

from .fishing import FishingLocations
from .market import MarketLocations

class Locations:
    fishing = FishingLocations()
    market = MarketLocations()
