from datetime import timedelta

from . import Plant

class Vegetables(Plant):
    pass

class Potato(Vegetables):
    required_level = 0
    growth_time = timedelta(minutes=5)

class Carrot(Vegetables):
    required_level = 0
    growth_time = timedelta(seconds=10)

class Tomato(Vegetables):
    required_level = 0
    growth_time = timedelta(minutes=5)

class Cucumber(Vegetables):
    required_level = 0
    growth_time = timedelta(minutes=5)
