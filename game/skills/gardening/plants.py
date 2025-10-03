from game.items import Item

class Plant(Item):
    cookable = True

class Carrots(Plant):
    name = 'Carrots'

class Tomatos(Plant):
    name = 'Tomatos'

class Cucumbers(Plant):
    name = 'Cucumbers'
