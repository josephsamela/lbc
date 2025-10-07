from .. import Skill

class Fishing(Skill):
    name = 'Fishing'
    description = "Join your fellow anglers as they go fishing and sell their catch for Lute Bear Coin!"

    def __init__(self):
        self.locations = [
            TributaryRiver(),
            OpenOcean(),
            Estuary(),
            CoralReef(),
        ]

from game.locations.fishing import *