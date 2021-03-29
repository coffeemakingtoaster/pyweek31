import pygame
from ..config import *
from ..superclasses import Actor

class Player(Actor.Actor):

    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.speed = 10
        self.inventory = dict()
        self.selected_item = None
    
    def update(self):
        if pygame.key.get_pressed()[PLAYER_MOVE_RIGHT] == True:
            self.x += self.speed 
        if pygame.key.get_pressed()[PLAYER_MOVE_DOWN] == True:
            self.y += self.speed 
        if pygame.key.get_pressed()[PLAYER_MOVE_LEFT] == True:
            self.x -= self.speed 
        if pygame.key.get_pressed()[PLAYER_MOVE_UP] == True:
            self.y -= self.speed 
        
        print("Player ", "x:" + str(self.x), "y: " + str(self.y))

    #call on item pickup    
    def add_item_to_inventory(item):
        self.inventory["item"] =self.inventory["item"] + 1
    
    #call on item drop/use
    def remove_item_to_inventory(item):
        self.inventory["item"] =self.inventory["item"] - 1

    #call on itemswitch
    def set_selected_item(item):
        if self.inventory["item"]>0:
            self.selected_item = item
        else:
            print("item is not in the players inventory")
            raise 

