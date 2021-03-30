from .game_objects import Chest
from .game_objects import Player
from .game_objects import Guard
from .game_objects import Wall
import pytmx

class Logic():
    def __init__(self, game_map):
        self.map = game_map
        
        self.chests = []
        self.chests.append(Chest.Chest())

        self.enemies = []
        self.enemies.append(Guard.Guard())
        self.player = Player.Player(self.chests)
        
        self.collision_objects = []
        
        self.add_collision_objects()

    def update(self):
        self.player.update()
        pass
        
    def add_collision_objects(self):
        for layer in self.map.visible_layers:
            if isinstance(layer, pytmx.TiledObjectGroup):
                # access collision object
                for obj in layer:
                # TODO: set wall positions
                    self.collision_objects.append(Wall.Wall())
                    # print(obj)
                    