from . import Location

from game.skills.fishing.actions import FishAction
from game.skills.fishing.fish import *

from game.skills.cooking.actions import CookAction

class MillRiver(Location):
    name = 'Mill River'
    description = "The Mill River is a cold & swift freshwater river that's home to several species of salmon!"
    activities = [
        FishAction(
            species=[
                PinkSalmon,
                CohoSalmon,
                SockeyeSalmon,
                ChinookSalmon
            ]
        )
    ]

class CozyCampfire(Location):
    name = 'Cozy Campfire'
    description = 'A shared cooking space where you can grill fresh-caught fish.'
    actions = [
        CookAction()
    ]

class CommunityGarden(Location):
    name = 'Community Garden'
    description = ''
    actions = []

class TrailheadCabin(Location):
    name = 'Trailhead Cabin'
    description = 'A cozy ranger outpost where you can craft trail signs, nature journals, wooden walking sticks, and other outdoorsy items using gathered materials.'
    actions = []

class SleepingGiant(Location):
    name = 'Sleeping Giant'
    description = ''
    locations = [
        MillRiver,       # Fishing
        CommunityGarden, # Gardening
        CozyCampfire,    # Cooking
        TrailheadCabin   # Crafting
    ]
