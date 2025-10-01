from . import Location

class GeneralStore(Location):
    name = 'General Store'

class TackleShop(Location):
    name = 'Bait & Tackle'

class MarketLocations:
    general_store = GeneralStore()
    tackle_shop = TackleShop()
