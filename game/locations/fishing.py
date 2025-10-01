from . import Location

class TributaryRiver(Location):
    name = 'TributaryRiver'

class OpenOcean(Location):
    name = 'Open Ocean'

class Estuary(Location):
    name = 'Estuary'

class CoralReef(Location):
    name = 'Coral Reef'

class FishingLocations:
    tributary_river = TributaryRiver
    open_ocean = OpenOcean
    estuary = Estuary
    coral_reef = CoralReef
