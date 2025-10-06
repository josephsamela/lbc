from .requirements import *
from .rewards import *

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
