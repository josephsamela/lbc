from . import *

class Nymph(Fly):
    pass

class PheasantTail(Nymph):
    required_level = 0
    xp = 10
    materials = [Bead, Feather, Wire]