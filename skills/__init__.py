from db import *

class SkillModel(Base):
    class Meta:
        db_table = 'skills'
    name = CharField(unique=True)

class Skill(Record):
    _model = SkillModel
