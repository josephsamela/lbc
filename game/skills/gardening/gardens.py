import datetime
import importlib
from db import Record, GardenModel

class Garden(Record):
    _model = GardenModel

    plant = None    # Seed Item Object
    stages = ['Seed', 'Growing', 'Harvest']
   
    @property
    def plant(self):
        # Return the item obj associated with this record.
        if hasattr(self, 'seed') and self.seed:
            name = self._record.seed.name.split(' ')[0]
            plants = importlib.import_module('game.skills.gardening.plants')
            return getattr(plants, name)()

    @property
    def growth_interval(self):
        if self.plant:
            return self.plant.growth_time / ( len(self.stages)-1 )

    @property
    def elapsed_time(self):
        if self.plant:
            return datetime.datetime.now() - self.planted_at

    @property
    def state(self):
        if not self.plant:
            return 'Empty'

        # Garden "state" is the number of growth intervals passed
        # have passed since planting.
        s = int( self.elapsed_time // self.growth_interval )

        if s >= len(self.stages):
            return self.stages[-1]

        return self.stages[s]

class CommunityGarden(Garden):
    name = 'Community Garden'
