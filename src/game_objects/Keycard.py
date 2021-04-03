import random
import pygame
from .. import Render
from ..config import *

class Keycards():

    keycard_spawns = [{"x_spawn":1568, "y_spawn":2275}, {"x_spawn":949, "y_spawn":1194}, {"x_spawn":1881, "y_spawn":652}, {"x_spawn":1880, "y_spawn":1530}, {"x_spawn":573, "y_spawn":630}]
    keycard_colors = ["blue", "red", "green"]
    

    def __init__(self, ui, spawn_rects):
        self.spawn_rects = spawn_rects
        self.ui = ui
        self.x = 40
        self.y = 40
        self.is_picked_up = False
        self.container = []
        self.create_keycards()
        self.all_collected = False
        self.collect_counter = 0
        self.cut_scene_called = False
    
    
    def create_keycards(self):
        for i in range(3):
            keycard_cords = random.choice(self.spawn_rects)
            #print(keycard_cords.x)
            self.spawn_rects.remove(keycard_cords)
            keycard_rect = pygame.Rect(keycard_cords.x,keycard_cords.y,30,30)
            self.container.append({"x_cord":keycard_rect.x, "y_cord":keycard_rect.y, "collectable":True, "rect":keycard_rect, "color":self.keycard_colors[i]})
        
    
    def keycard_player_collision(self, player_rect):
        if self.collect_counter <= 2:
            # print(self.collect_counter)
            for keycard in self.container:
                # print("schleife")
                if keycard["rect"].colliderect(player_rect):
                    if keycard["collectable"] == True:
                        # print("collided")
                        keycard["collectable"] = False
                        self.collect_counter += 1
                        self.ui.hud.player_keycards.append(keycard["color"])
                        #dialog stuff
                        if self.collect_counter == 1:
                            if not SKIP_DIALOGS:
                                self.ui.cut_scene.createCutScene([
                                    ['These corrupt cops left key cards laying around.', {}],
                                    ['Luckily I ain’t no white girl, this card’s dirty as hell.', {}],
                                    ['Guess the dog played with this one.', {}],
                                    ['Can’t remember his name tho...', {}],
                                    ['...think it was something with Y…', {}]
                                ])                            
                        # print(self.collect_counter)
        elif self.collect_counter >= 3:
            if not SKIP_DIALOGS and not self.cut_scene_called:
                self.ui.cut_scene.createCutScene([
                    ['This was the last one.', {}],
                    ['This trip was easier than handling git!', {}],
                    ['Who built this prison? A bunch of drunken students?!', {}],
                    ['Now I need to find the exit without being raped by aliens...', {}],
                    ['...although...heh', {}]
                ])
                self.cut_scene_called = True
            self.all_collected = True
            

