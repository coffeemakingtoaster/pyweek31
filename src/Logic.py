from .game_objects import Chest
from .game_objects import Player
from .game_objects import Guard
from .game_objects import Door
from .game_objects.helper.Point import Point
from .game_objects.helper.Section import Section
from .game_objects import Wall
from .game_objects.items.Coffee import Coffee
from .game_objects.items.Coin import Coin
from .game_objects.items.Donut import Donut
from .game_objects.items.Jammer import Jammer
from .game_objects import Keycard
from .game_objects import Mice

from . import config

import pytmx
import pygame

class Logic():

    def __init__(self, game_map, soundHelper, assets, game_state):

        self.game_state = game_state
        
        self.assets = assets
        
        self.soundHelper = soundHelper
        
        self.chests = []
        self.keycards = Keycard.Keycards()
        
        # this is moved here because it gets parsed below with the get_map_trigger... This is not good. 
        self.player_spawn_point = (1000, 1000)
        
        # trigger data
        self.enemy_waypoints = []
        self.map = game_map
        self.collision_objects = []
        self.hiding_spots = []

        # get all map trigger points
        self.get_map_trigger()

        self.doors = Door.Door_Container(self.map)

        self.walls = self.translate_collision_objects(self.collision_objects)
        self.player = Player.Player(self, self.chests, self.collision_objects, self.hiding_spots)
        self.enemies = []

        for enemy_waypoint in self.enemy_waypoints:
            #print(enemy_waypoint)

            self.enemies.append(Guard.Guard(enemy_waypoint['spawn_point'], self.walls, self.player, enemy_waypoint['waypoints'], {
                'type': enemy_waypoint['type'],
                'speed': enemy_waypoint['speed'],
                'logic': self
            }, game_state))

        self.coffee = Coffee(self)
        self.coin = Coin(self)
        self.donut = Donut(self)        

        self.mice = []
        self.mice.append(Mice.Mouse())
        self.mice.append(Mice.Mouse())
        
        self.jammer = Jammer(self)        

    def update(self):
        self.player.update()
        if self.player.has_moved:
            self.soundHelper.play_sfx(self.assets["sounds"]["actor"]["footsteps"]["concrete"],1)
        if self.doors.update(self.player, self.enemies):
            self.collision_objects = []
            self.walls = []
            self.refresh_walls()
        for keycard in self.keycards.container:
            keycard_rect = keycard["rect"]
            self.keycards.keycard_player_collision(self.player.player_hitbox)
        for enemy in self.enemies:
            enemy.update(self.walls)
            if self.game_state.is_over():
                self.soundHelper.play_gamestate_sfx(self.assets["sounds"]["caught"],1)    
        for mouse in self.mice:
            mouse.update()
        self.donut.snap_trap()
        if self.win_collide.colliderect(self.player.player_hitbox) and self.keycards.all_collected:
            print("victory")
            self.soundHelper.play_gamestate_sfx(self.assets["sounds"]["victory"],1) 
            self.game_state.set_game_state("victory")
        pass
                    
    def get_map_trigger(self):
        #print("checking for map triggers")
        for layer in self.map.visible_layers:
            if isinstance(layer, pytmx.TiledObjectGroup):
                for trigger_object in layer:
                    properties = trigger_object.__dict__
                    if properties["name"] == "'wall'":
                        x = properties['x'] * (config.TILE_SIZE/16)
                        y = properties['y'] * (config.TILE_SIZE/16)
                        width = properties['width'] * (config.TILE_SIZE/16)
                        height = properties['height'] * (config.TILE_SIZE/16)
                        wall = pygame.Rect(x, y, width, height)
                        self.collision_objects.append(wall)
                    elif properties["name"] == "'spawnpoint'":
                        self.player_spawn_point = (properties['x'] * (config.TILE_SIZE/16), properties['y'] * (config.TILE_SIZE/16))
                    elif properties["name"] == "'win_zone'":
                        x = properties['x'] * (config.TILE_SIZE/16)
                        y = properties['y'] * (config.TILE_SIZE/16)
                        width = properties['width'] * (config.TILE_SIZE/16)
                        height = properties['height'] * (config.TILE_SIZE/16)
                        self.win_collide = pygame.Rect(x, y, width, height)
                        # do something with win zone!!! 
                    elif properties["name"] == "waypoint":
                        enemy_waypoints = []
                        enemy_spawn_point = properties["points"][0]
            
                        # verify
                        if "'speed'" not in properties["properties"] or properties["properties"]["'speed'"] == "":
                            properties["properties"]["'speed'"] = "default"
                        
                        if properties["type"] == "" or properties["type"] is None:
                            properties["type"] = "default"

                        for point in properties["points"][1:]:
                            enemy_waypoints.append(point)
                        self.enemy_waypoints.append({
                            'spawn_point': enemy_spawn_point,
                            'waypoints': enemy_waypoints,
                            'type': properties["type"],
                            'speed': properties["properties"]["'speed'"]
                        })
                    elif properties["name"] == "hiding_spot":
                        x = properties['x'] * (config.TILE_SIZE/16)
                        y = properties['y'] * (config.TILE_SIZE/16)
                        width = properties['width'] * (config.TILE_SIZE/16)
                        height = properties['height'] * (config.TILE_SIZE/16)
                        spot = pygame.Rect(x, y, width, height)
                        self.hiding_spots.append(spot)
                    elif properties["name"] == "chest":
                        x = properties['x'] * (config.TILE_SIZE/16)
                        y = properties['y'] * (config.TILE_SIZE/16)
                        width = properties['width'] * (config.TILE_SIZE/16)
                        height = properties['height'] * (config.TILE_SIZE/16)
                        spot = pygame.Rect(x, y, width, height)
                        self.chests.append(Chest.Chest(spot))


    def refresh_walls(self):
        for layer in self.map.visible_layers:
            if isinstance(layer, pytmx.TiledObjectGroup):
                for trigger_object in layer:
                    properties = trigger_object.__dict__
                    if properties["name"] == "'wall'":
                        x = properties['x'] * (config.TILE_SIZE/16)
                        y = properties['y'] * (config.TILE_SIZE/16)
                        width = properties['width'] * (config.TILE_SIZE/16)
                        height = properties['height'] * (config.TILE_SIZE/16)
                        wall = pygame.Rect(x, y, width, height)
                        self.collision_objects.append(wall)
        self.walls = self.translate_collision_objects(self.collision_objects)    

    def translate_collision_objects(self,collision_objects):
        walls_as_sections = []
        for rect in collision_objects:
            walls_as_sections.append(Section(Point(rect.x,rect.y),Point(rect.x,rect.y+rect.height)))
            walls_as_sections.append(Section(Point(rect.x,rect.y),Point(rect.x+rect.width,rect.y)))
            walls_as_sections.append(Section(Point(rect.x,rect.y+rect.height), Point(rect.x + rect.width, rect.y+rect.height)))
            walls_as_sections.append(Section(Point(rect.x+rect.width,rect.y), Point(rect.x + rect.width, rect.y+rect.height)))
        return walls_as_sections

