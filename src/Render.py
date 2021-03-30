import pygame
from . import config

class Render(): 

    def __init__(self, logic, assets, gameMap):
        self.logic = logic
        self.assets = assets
        self.map = gameMap

    def generate_new_frame(self):
        self.frame = pygame.Surface(config.WINDOW_DIMENSIONS)
        self.draw_map()
        self.draw_game_objects()
        self.draw_hud()
        return self.frame

    #TODO: If there is more logic in map -> outsource this
    def draw_map(self):
        for layer in self.map.visible_layers:
            for x, y, gid, in layer:
                tile = self.map.get_tile_image_by_gid(gid)
                if tile != None:
                    self.frame.blit(tile, ( (x * self.map.tilewidth) - self.logic.player.x, (y * self.map.tileheight) - self.logic.player.y))
    
    def draw_game_objects(self):
        for enemy in self.logic.enemies:
            self.add_asset_to_screen(self.assets['textures']['enemy'], enemy.x , enemy.y)
        
        for chest in self.logic.chests:
            self.add_asset_to_screen(self.assets['textures']['chest'], chest.x, chest.y)
        #draw player                        
        self.add_asset_to_screen(self.assets['textures']['max'])
        
    
    def add_asset_to_screen(self,asset, x = None, y = None):
        if not x:
            x = config.WINDOW_WIDHT/2
        else: 
            x = x - self.logic.player.x
        if not y:
            y = config.WINDOW_HEIGHT/2
        else: 
            y = y - self.logic.player.y
        self.frame.blit(asset, ( x  - asset.get_width()/2 , y  - asset.get_height()/2))
    
    def draw_hud(self):
        font = pygame.font.SysFont(None, 24)
        img = font.render('hello', True, (0, 0, 255))
        self.frame.blit(img, (20, 20))

    def tile_is_onscreen(self,x,y):
        if not (self.logic.player.x - config.WINDOW_WIDHT/2) <= x <= (self.logic.player.x + config.WINDOW_WIDHT/2):
            return False
        if not (self.logic.player.y - config.WINDOW_HEIGHT/2) <= y <= (self.logic.player.y + config.WINDOW_HEIGHT/2):
            return False
        return True