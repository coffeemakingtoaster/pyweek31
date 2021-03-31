import pygame
from . import config
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
                        self.frame.blit(tile, ( (x * config.TILE_SIZE) - self.logic.player.x, (y * config.TILE_SIZE) - self.logic.player.y))

    
    def draw_game_objects(self):
        for enemy in self.logic.enemies:
            self.add_asset_to_screen(self.assets['textures']['enemy'], enemy.x , enemy.y)
        
        for chest in self.logic.chests:
            self.add_asset_to_screen(pygame.transform.scale(self.assets['textures']['chest'],(config.TILE_SIZE,config.TILE_SIZE)), chest.x, chest.y)
        #draw player
        player = pygame.transform.scale(pygame.transform.rotate(self.assets['textures']['max'], self.logic.player.rotation),(config.TILE_SIZE,config.TILE_SIZE))                      
        self.add_asset_to_screen(player)
        
    
    def add_asset_to_screen(self,asset, x = None, y = None):
        if not x:
            x = config.WINDOW_WIDHT/2
        else: 
            x = x - self.logic.player.x + config.WINDOW_WIDHT/2
        if not y:
            y = config.WINDOW_HEIGHT/2
        else: 
            y = y - self.logic.player.y + config.WINDOW_HEIGHT/2
        self.frame.blit(asset, ( x  - asset.get_width()/2 , y  - asset.get_height()/2))
    
    def tile_is_onscreen(self,x,y):
        if not (self.logic.player.x - config.TILE_SIZE) <= (x * config.TILE_SIZE) <= (self.logic.player.x + config.WINDOW_WIDHT):
            return False
        if not (self.logic.player.y - config.TILE_SIZE) <= (y* config.TILE_SIZE) <= (self.logic.player.y + config.WINDOW_HEIGHT):
            return False
        return True
    
    def get_drawn_frames(self):
        x = self.cnt
        self.cnt = 0
        return x
   
