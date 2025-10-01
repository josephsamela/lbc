import random

class Fish:
    def __init__(self):
        relative_size = random.random()
        self.weight_lb = relative_size * self.max_weight_lb
        self.length_in = relative_size * self.max_length_in

class PinkSalmon(Fish):
    name = 'Pink Salmon'
    icon='salmon_pink.png'
    max_weight_lb=15
    max_length_in=30

class CohoSalmon(Fish):
    name = 'Coho Salmon'
    icon='salmon_coho.png'
    max_weight_lb=36
    max_length_in=42

class SockeyeSalmon(Fish):
    name = 'Sockeye Salmon'
    icon='salmon_sockeye.png'
    max_weight_lb=15
    max_length_in=30

class ChinookSalmon(Fish):
    name = 'Chinook Salmon'
    icon='salmon_chinook.png'
    max_weight_lb=80
    max_length_in=60

class FishSpecies:
    pink_salmon = PinkSalmon
    coho_salmon = CohoSalmon
    sockeye_salmon = SockeyeSalmon
    chinook_salmon = ChinookSalmon
