import random
import pygame
from . import Render

class Keycards():


    def __init__(self):
        self.x = 40
        self.y = 40
        self.is_picked_up = False
        self.container = []
    
    #container = []

    #asset for keycard
    
    
    def create_keycards(self):
        self.keycard_posx = random.randrange(100, 800)
        self.keycard_posy = random.randrange(100, 800)
        return [self.keycard_posx, self.keycard_posy]
