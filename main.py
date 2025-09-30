from game import Game
from players import Player

game = Game()

joe = Player(username='joe')
jamie = Player(username='jamie')

c = game.items.lures.Crankbait()
f = game.items.fish.PinkSalmon()

joe.inventory.count(c)
joe.inventory.check(c, 1)
joe.inventory.check(c, 10)
joe.inventory.add(c, 2)
joe.inventory.remove(c, 1)

print('hello')
