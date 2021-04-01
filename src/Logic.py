from .game_objects import Chest
from .game_objects import Player
from .game_objects import Guard
from .game_objects.helper.Point import Point
from .game_objects.helper.Section import Section
from .game_objects import Wall

import pytmx
import pygame

class Logic():
    def __init__(self, game_map):
        self.chests = []
        self.chests.append(Chest.Chest())
        
        self.map = game_map
        self.collision_objects = []
        self.add_collision_objects()
        self.walls = self.translate_collision_objects(self.collision_objects)
        self.enemies = []
        self.enemies.append(Guard.Guard(Point(200,200),self.walls))
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

    def translate_collision_objects(self,collision_objects):
        walls_as_sections = []
        for rect in collision_objects:
            walls_as_sections.append(Section(Point(rect.x,rect.y),Point(rect.x,rect.y+rect.height)))
            walls_as_sections.append(Section(Point(rect.x,rect.y),Point(rect.x+rect.width,rect.y)))
            walls_as_sections.append(Section(Point(rect.x,rect.y+rect.height), Point(rect.x + rect.width, rect.y+rect.height)))
            walls_as_sections.append(Section(Point(rect.x+rect.width,rect.y), Point(rect.x + rect.width, rect.y+rect.height)))
        return walls_as_sections

