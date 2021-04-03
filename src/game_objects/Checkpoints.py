import pygame
import copy

class Checkpoint():
    def __init__(self,logic,rect):
        self.hitbox = rect
        self.logic = logic
        self.used = False
        
    def save_gamestate(self,player):
        self.player_pos = (player.x, player.y)
        return self
        