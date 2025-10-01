from game import Game
from player import Player

game = Game()

p = Player(username='joe', password='12345')

# Test balance

p.balance = 0
print(f'{p.username} has {p.balance} LBC.')

p.balance += 10
print(f'Add 10. {p.username} has {p.balance} LBC.')

p.balance += 4
print(f'Add 4. {p.username} has {p.balance} LBC.')

p.balance -= 2
print(f'Subtract 2. {p.username} has {p.balance} LBC.')

# Test inventory

i = game.items.lures.crankbait
print(f'{p.username} has {p.inventory.count(i)} {i.name}.')

p.inventory.add(i, quantity=3)
print(f'Add 3. {p.username} has {p.inventory.count(i)} {i.name}.')

p.inventory.remove(i, quantity=2)
print(f'Subtract 2. {p.username} has {p.inventory.count(i)} {i.name}.')

# Test skill experience

s = game.skills.fishing

xp = p.experience.count(s)
level = p.experience.level(s)

next_level = p.experience.next_level(s)
xp_remaining = p.experience.xp_remaining(s)
progress = p.experience.next_level_progress(s)

print('stop')
