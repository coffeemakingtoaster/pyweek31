import pygame
from . import config

class Render(): 

    def __init__(self, logic, assets):
        self.logic = logic
        self.assets = assets

    def generate_new_frame(self):
        self.frame = pygame.Surface(config.WINDOW_DIMENSIONS)

        self.frame.blit(self.assets['textures']['max'], (self.logic.player.x, self.logic.player.y))

        return self.frame
