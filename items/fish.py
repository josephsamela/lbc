from . import Fish

class PinkSalmon(Fish):
    name = 'Pink Salmon'
    icon='salmon_pink.png'
    max_weight_lbs=15
    max_length_in=30

class CohoSalmon(Fish):
    name = 'Coho Salmon'
    icon='salmon_coho.png'
    max_length_in=42
    max_weight_lbs=36

class SockeyeSalmon(Fish):
    name = 'Sockeye Salmon'
    icon='salmon_sockeye.png'
    max_length_in=30
    max_weight_lbs=15

class ChinookSalmon(Fish):
    name = 'Chinook Salmon'
    icon='salmon_chinook.png'
    max_length_in=60
    max_weight_lbs=80
