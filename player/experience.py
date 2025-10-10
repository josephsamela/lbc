from db import ExperienceModel

class ExperienceManager:
    def __init__(self, player):
        self.player = player
        self.xp_curve = 4.00874870400014

    def count(self, skill):
        '''
        Return player experience in skill
        '''
        if not skill in ['fishing', 'gardening', 'cooking', 'crafting']:
            raise Exception('Not a valid skill')

        r,c = ExperienceModel.get_or_create(
            player=self.player._record, 
            skill=skill
        )
        return r.quantity

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
        # Calc total xp required to go from current level to next level
        xp_curr_lvl = self._xp_from_level(self.level(skill))
        xp_next_lvl = self._xp_from_level(self.next_level(skill))
        total_xp_req = xp_next_lvl - xp_curr_lvl
        
        # Calc xp acquired since current level
        xp_acquired = self.count(skill) - xp_curr_lvl

        # Return % complete as decimal
        return xp_acquired / total_xp_req

    def add(self, skill, quantity=1):
        '''
        Add experience to player skill
        '''
        r,c = ExperienceModel.get_or_create(
            player=self.player._record, 
            skill=skill
        )
        r.quantity += quantity
        r.save()
