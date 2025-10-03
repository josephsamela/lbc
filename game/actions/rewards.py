
class Rewards:
    pass

class ItemReward(Rewards):
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

    def grant(self, player):
        '''
        Give player item reward
        '''
        player.inventory.add(
            item=self.item, 
            quantity=self.quantity
        )

class ExperienceReward(Rewards):
    def __init__(self, skill, quantity):
        self.skill = skill
        self.quantity = quantity
    
    def grant(self, player):
        '''
        Give player experience reward
        '''
        player.experience.add(
            skill=self.skill, 
            quantity=self.quantity
        )
