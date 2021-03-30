from .game_objects import Chest
from .game_objects import Player
from .game_objects import Guard

class Logic():
    def __init__(self):
        self.chests = []
        self.chests.append(Chest.Chest())

        self.enemies = []
        self.enemies.append(Guard.Guard())
        self.player = Player.Player(self.chests)


    def update(self):
        self.player.update()
        pass