import pygame
from . import config
from .helper import GraphicsHelper
import pytmx
import math 

class Render(): 

    def __init__(self, logic, assets, gameMap, ui):
        self.logic = logic
        self.assets = assets
        self.map = gameMap
        self.ui = ui
        self.cnt = 0
        self.tiles_on_screen = 0

    def generate_new_frame(self):
        self.frame = pygame.Surface(config.WINDOW_DIMENSIONS)
        self.draw_map()
        self.draw_game_objects()
        self.ui.draw_ui(self)
        self.cnt+=1
        self.tiles_on_screen = 0
        return self.frame

    def draw_map(self):            
        for layer in self.map.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = self.map.get_tile_image_by_gid(gid)              
                    if tile != None and self.tile_is_onscreen(x, y ):
                        tile = pygame.transform.scale(tile,(config.TILE_SIZE,config.TILE_SIZE))
                        self.frame.blit(tile, ( (x * config.TILE_SIZE) - self.logic.player.x + config.WINDOW_WIDHT/2  , (y * config.TILE_SIZE) - self.logic.player.y + config.WINDOW_HEIGHT/2))

        #this displays hitboxes
        if not config.DEBUG_DRAW_COLLISION:
            return
        for layer in self.map.visible_layers:
            if isinstance(layer, pytmx.TiledObjectGroup):
                #access collision object
                pygame.draw.rect(self.frame,(0,0,255),((0 * (config.TILE_SIZE/16)) - self.logic.player.x, (0 * (config.TILE_SIZE/16)) - self.logic.player.y,150,150))
                for collision_object in layer:
                    properties = collision_object.__dict__
                    if properties["name"] == "'wall'":
                        width = properties['width'] * (config.TILE_SIZE/16)
                        height = properties['height'] * (config.TILE_SIZE/16)
                        pygame.draw.rect(self.frame,(255,0,0),((properties['x'] * (config.TILE_SIZE/16)) - self.logic.player.x + config.WINDOW_WIDHT/2, (properties['y'] * (config.TILE_SIZE/16)) - self.logic.player.y + config.WINDOW_HEIGHT/2,width,height))

    
    def draw_game_objects(self):
        for enemy in self.logic.enemies:
            enemy_visual = GraphicsHelper.render_helper.rotate_image(self.assets['textures']['enemy'], enemy.rotation)
            debug_string = ""
            last_v_length = 0
            for ray in enemy.intersections:
                v = pygame.Vector2(ray.x - enemy.pos.x, ray.y - enemy.pos.y)
                if v.length() != last_v_length:
                    debug_string += " {} (x: {}, y:{})\n".format(v.length(),ray.x, ray.y)
                    last_v_length = v.length()
                start = (enemy.pos.x - self.logic.player.x  + config.WINDOW_WIDHT/2, enemy.pos.y - self.logic.player.y  + config.WINDOW_HEIGHT/2)
                end = (ray.x - self.logic.player.x  + config.WINDOW_WIDHT/2, ray.y - self.logic.player.y  + config.WINDOW_HEIGHT/2)          
                pygame.draw.line(self.frame,(0,0,255),start,end)
            enemy_visual = pygame.transform.scale(enemy_visual,(config.TILE_SIZE,config.TILE_SIZE)) 
            self.add_asset_to_screen(enemy_visual, enemy.pos.x , enemy.pos.y)
            print(debug_string  )
        for chest in self.logic.chests:
            self.add_asset_to_screen(pygame.transform.scale(self.assets['textures']['chest'],(config.TILE_SIZE,config.TILE_SIZE)), chest.x, chest.y)
        #draw player
        player = GraphicsHelper.render_helper.rotate_image(self.assets['textures']['max'], self.logic.player.rotation)
        player = pygame.transform.scale(player,(config.TILE_SIZE,config.TILE_SIZE))                      
        self.add_asset_to_screen(player)
              
    
    def add_asset_to_screen(self,asset, x = None, y = None):
        if not x:
            x = config.WINDOW_WIDHT/2
        else: 
            x = x - self.logic.player.x  + config.WINDOW_WIDHT/2
        if not y:
            y = config.WINDOW_HEIGHT/2
        else: 
            y = y - self.logic.player.y  + config.WINDOW_HEIGHT/2
        self.frame.blit(asset, ( x  - asset.get_width()/2 , y  - asset.get_height()/2))
    
    def tile_is_onscreen(self,x,y):
        if not (self.logic.player.x - config.TILE_SIZE - config.WINDOW_WIDHT) <= (x * config.TILE_SIZE) <= (self.logic.player.x + config.WINDOW_WIDHT):
            return False
        if not (self.logic.player.y - config.TILE_SIZE - config.WINDOW_HEIGHT) <= (y* config.TILE_SIZE) <= (self.logic.player.y + config.WINDOW_HEIGHT):
            return False
        return True
    
    def get_drawn_frames(self):
        x = self.cnt
        self.cnt = 0
        return x
   
