from . import *

from skills import SkillModel

class ExperienceModel(Base):
    class Meta:
        db_table = 'experience'
    skill = ForeignKeyField(SkillModel)
    player = ForeignKeyField(PlayerModel)
    quantity = IntegerField(default=0)

class SkillExperience(Record):
    _model = ExperienceModel

class Experience:
    def __init__(self, player):
        self.player = player

    def total(self, skill):
        '''
        Return amount of experience player has in skill
        '''
        return SkillExperience(
            player=self.player, 
            skill=skill
        ).quantity

    def add(self, skill, quantity=1):
        '''
        Add experience to player skill
        '''
        SkillExperience(
            player=self.player, 
            skill=skill
        ).quantity += quantity
