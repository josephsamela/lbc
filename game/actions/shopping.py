from . import *

class BuyAction(Action):

    def __init__(self, resources):
        # Dict of items for sale
        self.resources = resources

    @property
    def requirements(self):
        return [
            BalanceRequirement(
                quantity=1
            )
        ]

    @property
    def rewards(self):
        if self.fish:
            return [
                ItemReward(
                    item=self.fish,
                    quantity=1
                ),
                ExperienceReward(
                    skill=self.skill,
                    quantity=self.fish.xp
                )
            ]
        return []

    def execute(self, game, player, target, *args, **kwargs):
        self.item = game.items.get(target)

        if not target in self.resources:
            raise Exception(f'{self.item.name} is not for sale.')


        super().execute(player)

