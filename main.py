from game.skills.fishing.fish import PinkSalmon
from game.skills.cooking.food import Milk, Egg, Flour
from game.skills.cooking.recipes import Cake

from game.skills import Cooking

from game.skills.cooking.actions import CookItem, CookRecipe, CookAction
from player import Player

p = Player(username='joe', password='12345')
# ci = CookItem()

ca = CookAction()

# Test Cook Item
f = PinkSalmon()
p.inventory.drop(f)
while True:

    p.inventory.add(f)

    fr_count = p.inventory.count(f.raw())
    fc_count = p.inventory.count(f.cooked())
    fb_count = p.inventory.count(f.burnt())

    result = ca.execute(
        player=p,
        item=f
    )

    print(f'Result: {result.name}. {p.username} has {fc_count} Cooked & {fb_count} Pink Salmon. Level {p.experience.level(Cooking)} Cooking. {round(p.experience.next_level_progress(Cooking)*100)}% to {p.experience.next_level(Cooking)}. {p.experience.count(Cooking)} Cooking xp.')


egg = Egg()
flour = Flour()
milk = Milk()

# Test Cook Recipe
p.inventory.drop(milk)
p.inventory.drop(egg)
p.inventory.drop(flour)

# cr = CookRecipe()
r = Cake()

while True:
    p.inventory.add(milk)
    p.inventory.add(egg)
    p.inventory.add(flour)

    fc_count = p.inventory.count(r.cooked())
    fb_count = p.inventory.count(r.burnt())

    result = ca.execute(
        player=p,
        recipe=r
    )

    print(f'Result: {result.name}. {p.username} has {fc_count} Cooked & {fb_count} Burnt Cake. Level {p.experience.level(Cooking)} Cooking. {round(p.experience.next_level_progress(Cooking)*100)}% to {p.experience.next_level(Cooking)}. {p.experience.count(Cooking)} Cooking xp.')
