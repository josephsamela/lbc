from db import Record, ExperienceModel

class ExperienceSlot(Record):
    _model = ExperienceModel

class ExperienceManager:
    def __init__(self, player):
        self.player = player
        self.xp_curve = 4.00874870400014

    def count(self, skill):
        '''
        Return player experience in skill
        '''
        return ExperienceSlot(
            player=self.player, 
            skill=skill
        ).quantity

    def _level_from_xp(self, xp):
        '''
        Calculate level from experience
        '''
        return int(xp ** (1/self.xp_curve))
    
    def _xp_from_level(self, level):
        '''
        Calculate experience from level
        '''
        return int(level ** self.xp_curve)

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
        xp_curr_lvl = self._xp_from_level(self.level(skill))
        xp_next_lvl = self._xp_from_level(self.next_level(skill))
        total_xp_req = xp_next_lvl - xp_curr_lvl
        xp_acquired = total_xp_req - self.xp_remaining(skill)
        return xp_acquired / total_xp_req

    def add(self, skill, quantity=1):
        '''
        Add experience to player skill
        '''
        ExperienceSlot(
            player=self.player, 
            skill=skill
        ).quantity += quantity
