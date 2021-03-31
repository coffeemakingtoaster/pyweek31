from .game_objects import Chest
from .game_objects import Player
from .game_objects import Guard
from .game_objects.helper.Point import *
from .game_objects import Wall
import pytmx
import pygame

class Logic():
    def __init__(self):
        self.chests = []
        self.chests.append(Chest.Chest())

        self.enemies = []
        self.enemies.append(Guard.Guard(Point(200,200)))
        self.player = Player.Player(self.chests)


    def update(self):
        self.player.update()
        for enemy in self.enemies:
            enemy.update()
        pass

    def add_collision_objects(self):
        for layer in self.map.visible_layers:
            if isinstance(layer, pytmx.TiledObjectGroup):
                # access collision object
                for collision_object in layer:
                    properties = collision_object.__dict__
                    if properties['name'] == 'wall':
                        x = properties['x']
                        y = properties['y']
                        width = properties['width']
                        height = properties['height']
                        wall = pygame.Rect(x, y, width, height)
                        self.collision_objects.append(wall)

