from game.skills.fishing.fish import PinkSalmon
from game.skills.cooking.food import Milk, Egg, Flour
from game.skills.cooking.recipes import Cake

from game.skills.cooking.actions import CookItem, CookRecipe
from player import Player

p = Player(username='joe', password='12345')
f = PinkSalmon()

# Test Cook Item
p.inventory.drop(f)
p.inventory.add(f)

ci = CookItem()
ci.execute(
    player=p,
    item=f
)

# Test Cook Recipe
p.inventory.drop(Milk)
p.inventory.drop(Egg)
p.inventory.drop(Flour)

p.inventory.add(Milk)
p.inventory.add(Egg)
p.inventory.add(Flour)

cr = CookRecipe()

cr.execute(
    player=p,
    recipe=Cake
)
