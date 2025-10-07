from . import FishingLocation

from game.skills.fishing.fish import *

class TributaryRiver(FishingLocation):
    description = "The Tributary River is a cold & swift freshwater river that's home to several species of salmon!"
    fish = [
        PinkSalmon,
        CohoSalmon,
        SockeyeSalmon,
        ChinookSalmon,
    ]

class OpenOcean(FishingLocation):
    description = "The Open Ocean is a rough saltwater marine environment with many species of large fish!"
    fish = [
        PinkSalmon,
        CohoSalmon,
        SockeyeSalmon,
        ChinookSalmon,
    ]

class Estuary(FishingLocation):
    description = "The Estuary is a coastal brakish environment that's home to many diverse species of fish!"
    fish = [
        PinkSalmon,
        CohoSalmon,
        SockeyeSalmon,
        ChinookSalmon,
    ]

class CoralReef(FishingLocation):
    description = "The Coral Reef is a vibrant warmwater marine ecosystem with many colorful and unique fish!"
    fish = [
        PinkSalmon,
        CohoSalmon,
        SockeyeSalmon,
        ChinookSalmon,
    ]
