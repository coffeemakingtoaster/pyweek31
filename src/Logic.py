from .game_objects import Chest
from .game_objects import Player
from .game_objects import Guard
from .game_objects.helper.Point import *

class Logic():
    def __init__(self):
        self.chests = []
        self.chests.append(Chest.Chest())

        self.enemies = []
        self.enemies.append(Guard.Guard(Point(200,200))
        self.player = Player.Player(self.chests)


    def update(self):
        self.player.update()
        for enemy in self.enemies:
            enemy.update()
        pass
