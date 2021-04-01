import pygame
from . import config
import pytmx

class Render(): 

    def __init__(self, logic, assets, gameMap, ui, keycard):
        self.logic = logic
        self.assets = assets
        self.map = gameMap
        self.ui = ui
        self.cnt = 0
        self.keycard = keycard

    def generate_new_frame(self):
        self.frame = pygame.Surface(config.WINDOW_DIMENSIONS)
        self.draw_map()
        self.draw_game_objects()
        self.ui.draw_ui(self)
        self.cnt+=1
        return self.frame

    def draw_map(self):            
        for layer in self.map.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = self.map.get_tile_image_by_gid(gid)              
                    if tile != None:
                        tile = pygame.transform.scale(tile,(config.TILE_SIZE,config.TILE_SIZE))
                        self.frame.blit(tile, ( (x * config.TILE_SIZE) - self.logic.player.x, (y * config.TILE_SIZE) - self.logic.player.y))

    
    def draw_game_objects(self):
        for enemy in self.logic.enemies:
            self.add_asset_to_screen(self.assets['textures']['enemy'], enemy.x , enemy.y)
        
        for chest in self.logic.chests:
            self.add_asset_to_screen(pygame.transform.scale(self.assets['textures']['chest'],(config.TILE_SIZE,config.TILE_SIZE)), chest.x, chest.y)
        
        for keycard in self.keycard.container:
            player_asset = self.assets['textures']['max']
            player_rect = pygame.Rect((self.logic.player.x, self.logic.player.y),(50,50))
            player_rect.center=(self.logic.player.x, self.logic.player.y)
            if keycard["collectable"]: 
                key_x = keycard["x_cord"]
                key_y = keycard["y_cord"]
                self.add_asset_to_screen(self.assets['textures']['keycard'], key_x, key_y)
            keycard_rect = keycard["rect"]
        self.keycard.keycard_player_collision(keycard_rect, player_rect)

        #draw player                        
        self.add_asset_to_screen(self.assets['textures']['max'])

        #draw rect around player
        player_asset = self.assets['textures']['max']
        player_rect = player_asset.get_rect
    
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
        if not (self.logic.player.x - config.WINDOW_WIDHT) <= (x*self.map.tilewidth) <= (self.logic.player.x + config.WINDOW_WIDHT):
            return False
        if not (self.logic.player.y - config.WINDOW_HEIGHT) <= (y*self.map.tileheight) <= (self.logic.player.y + config.WINDOW_HEIGHT):
            return False
        return True
    
    def get_drawn_frames(self):
        x = self.cnt
        self.cnt = 0
        return x
