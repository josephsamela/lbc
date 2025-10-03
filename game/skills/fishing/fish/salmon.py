from . import Fish
from ..bait import *

class Salmon(Fish):
    required_bait = [Jig, Spoon, WoolyBugger]

class PinkSalmon(Salmon):
    required_level = 0
    xp = 10

class CohoSalmon(Salmon):
    required_level = 5
    xp = 20

class SockeyeSalmon(Salmon):
    required_level = 10
    xp = 30

class ChinookSalmon(Salmon):
    required_level = 20
    xp = 40
