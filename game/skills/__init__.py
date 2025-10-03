from db import Record, SkillModel

class Skill(Record):
    _model = SkillModel

from .fishing import Fishing
from .gardening import Gardening
from .cooking import Cooking
from .crafting import Crafting
