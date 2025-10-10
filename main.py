import datetime

from db import *

# Create db tables if they don't exist
for model in [ItemModel, PlayerModel, InventoryModel, ExperienceModel]:
    if not db.table_exists(model):
        model.create_table()

# Once db is created, initialize game
from game import Game
game = Game()

from game.items import *

from player import Player
player = Player(username='joe', password='12345', session_token='abc', session_expiration=datetime.datetime.now())
player = Player(username='joe')

# Test Experience
# assert player.journal.discovered(salmon) == False
# player.journal.discover(salmon)
# assert player.journal.discovered(salmon) == True

# Test Inventory
f = raw_pink_salmon
player.inventory.check(f)
player.inventory.drop(f)
assert player.inventory.count(f) == 0
player.inventory.add(f)
player.inventory.add(f, quantity=5)
assert player.inventory.count(f) == 6
player.inventory.remove(f, quantity=3)
assert player.inventory.count(f) == 3
player.inventory.items()

# Test Experience
skill = 'Fishing'
player.experience.count(skill)
player.experience.level(skill)
player.experience.next_level(skill)
player.experience.xp_remaining(skill)
player.experience.next_level_progress(skill)
player.experience.add(skill, quantity=100)

# Test Fishing
fa = game.locations['tributary_river']['actions'][0]
b = meal_worms
player.inventory.add(b)
fa.execute(player, b)

# Test Cooking
ca = game.locations['cozy_campfire']['actions'][0]
ca.execute(player, cooked_pink_salmon)
player.inventory.add(flour)
player.inventory.add(egg)
player.inventory.add(milk)
ca.execute(player, cake)


# Test Crafting
cr = game.locations['craft_pavilion']['actions'][0]
player.inventory.add(bead)
player.inventory.add(feather)
player.inventory.add(wire)
cr.execute(player, pheasant_tail)
