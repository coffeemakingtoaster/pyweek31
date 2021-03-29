from .game_objects import Chest
from .game_objects import Player

class Logic():
    def __init__(self):
        self.chests = []
        self.chests.append(Chest.Chest())


        self.enemies = []
        self.player = Player.Player()


    def update(self):
        self.player.update()
        pass