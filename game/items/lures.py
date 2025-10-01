from ..items import Item

class Lure(Item):
    pass

class Crankbait(Lure):
    name = 'Crankbait'

class Popper(Lure):
    name = 'Popper'

class Spinner(Lure):
    name = 'Spinner'

class Lures:
    crankbait = Crankbait
    popper = Popper
    spinner = Spinner
