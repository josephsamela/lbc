
class Action:
    requirements = []
    rewards = []

    def _check_requirements(self, player):
        '''
        Check player meets requirements
        '''
        for requirement in self.requirements:
            if not requirement.check(player):
                raise Exception(requirement.note)
        return True

    def _consume_resources(self, player):
        '''
        Remove required items from inventory
        '''
        for requirement in self.requirements:
            if isinstance(requirement, ItemRequirement):
                player.inventory.remove(
                    item=requirement.item,
                    quantity=requirement.quantity
                )

    def _grant_rewards(self, player):
        '''
        Grant player rewards
        '''
        for reward in self.rewards:
            reward.grant(player)

    def execute(self, player):
        '''
        Execute action

        Actions always follow the same three steps.

        1. Check if player meets requirements to perform this action. (ie. Level, Items)
        2. Remove any resources consumed by this action from player inventory.
        3. Grant player rewards produced by this action (ie. Items, Experience).

        '''
        self._check_requirements(player)
        self._consume_resources(player)
        self._grant_rewards(player)

class ItemRequirement:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity
        self.note = f'Requires {quantity} {item.name}.'

    def check(self, player):
        '''
        Check if player has required item quantity
        '''
        return player.inventory.check(self.item, self.quantity)
        
class LevelRequirement:
    def __init__(self, skill, level):
        self.skill = skill
        self.level = level
        self.note = f'Requires {level} {skill}.'

    def check(self, player):
        '''
        Check if player has required skill level
        '''
        if player.experience.level(self.skill) >= self.level:
            return True
        else:
            return False

class ItemReward:
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

class ExperienceReward:
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
