
class Requirements:
    pass

class ItemRequirement(Requirements):
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity
        self.note = f'Requires {quantity} {item.name}.'

    def check(self, player):
        '''
        Check if player has required item quantity
        '''
        return player.inventory.check(self.item, self.quantity)
        
class LevelRequirement(Requirements):
    def __init__(self, skill, level):
        self.skill = skill
        self.level = level
        self.note = f'Requires {level} {skill.name}.'

    def check(self, player):
        '''
        Check if player has required skill level
        '''
        if player.experience.level(self.skill) >= self.level:
            return True
        else:
            return False
