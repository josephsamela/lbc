import random

class Plant:
    def __init__(self):
        pass

class Carrots(Plant):
    name = 'Carrots'

class Tomatos(Plant):
    name = 'Tomatos'

class Cucumbers(Plant):
    name = 'Cucumbers'

class PlantSpecies:
    carrots = Carrots
    tomatos = Tomatos
    cucumbers = Cucumbers
