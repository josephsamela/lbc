from db import Record, ExperienceModel

class ExperienceSlot(Record):
    _model = ExperienceModel

class ExperienceManager:
    def __init__(self, player):
        self.player = player

    def count(self, skill):
        '''
        Return player experience in skill
        '''
        return ExperienceSlot(
            player=self.player, 
            skill=skill
        ).quantity

    def _level_from_xp(self, xp):
        return int(xp ** 0.249454399324694)
    
    def _xp_from_level(self, level):
        return int(level ** 4.00874870400014)

    def level(self, skill):
        '''
        Return player level in skill
        '''
        return self._level_from_xp(
            self.count(skill)
        )

    def next_level(self, skill):
        '''
        Return player next level in skill
        '''
        return self.level(skill)+1

    def xp_remaining(self, skill):
        '''
        Return player xp remaining to reach next level
        '''
        current_xp = self.count(skill)
        required_xp = self._xp_from_level(self.next_level(skill))
        return required_xp - current_xp
    
    def next_level_progress(self, skill):
        '''
        Return player % progress to next level
        '''
        return self.count(skill) / self._xp_from_level(self.next_level(skill))

    def add(self, skill, quantity=1):
        '''
        Add experience to player skill
        '''
        ExperienceSlot(
            player=self.player, 
            skill=skill
        ).quantity += quantity
