import importlib
import os
from db import db

class Game:
    def __init__(self):

        self.items = self.load('items')
        self.skills = self.load('skills')
        self.locations = self.load('locations')

    def load(self, package):
        '''
        This method loads game objects.

        Game objects are organized into packages    (ie. items).
        Game packages contain modules               (ie. baits, lures)
        Game modules contain objects                (ie. Crankbait, Nightcrawlers, etc.)
        .
        └── items
            ├── baits.py
            │   ├── Mealworms
            │   ├── Nightcrawlers
            │   ├── Crickets
            └── lures.py
                ├── Crankbait
                ├── Popper
                └── Spinner

        This method loads target package making objects accessible like: `package.module.object`
        '''
        # Generate list of modules to load
        modules = []
        for module in os.listdir(package):
            if not module.startswith('_') and not module.startswith('.'):
                modules.append(
                    module.split('.py')[0]
                )

        # Load classes from each module
        i = Folder()
        for module in modules:
            j = Folder()
            m = importlib.import_module(f'{package}.{module}')
            for k,v in m.__dict__.items():
                if hasattr(v ,'__module__') and v.__module__ == f'{package}.{module}':
                    setattr(j,k,v)
            setattr(i,module,j)

        return i

class Folder: pass
