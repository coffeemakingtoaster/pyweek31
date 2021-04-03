import random
import pygame
from .. import Render

class Keycards():

    keycard_spawns = [{"x_spawn":1568, "y_spawn":2275}, {"x_spawn":949, "y_spawn":1194}, {"x_spawn":1881, "y_spawn":652}, {"x_spawn":1880, "y_spawn":1530}, {"x_spawn":573, "y_spawn":630}]
    keycard_colors = ["blue", "red", "green"]
    collect_counter = 0

    def __init__(self, ui):
        self.ui = ui
        self.x = 40
        self.y = 40
        self.is_picked_up = False
        self.container = []
        self.create_keycards()
    
    
    def create_keycards(self):
        for i in range(3):
            keycard_pos = random.choice(self.keycard_spawns)
            keycard_posx = keycard_pos["x_spawn"]
            keycard_posy = keycard_pos["y_spawn"]
            keycard_rect = pygame.Rect((0,0),(30,30))
            keycard_rect.center = (keycard_posx,keycard_posy)
            self.container.append({"x_cord":keycard_posx, "y_cord":keycard_posy, "collectable":True, "rect":keycard_rect, "color":self.keycard_colors[i]})
        
    
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
                        
                        #dialog stuff
                        if self.collect_counter == 1:
                            self.ui.cut_scene.createCutScene([
                                ['These corrupt cops left key cards laying around.', {}],
                                ['Luckily I ain’t no white girl, this card’s dirty as hell.', {}],
                                ['Guess the dog played with this one.', {}],
                                ['Can’t remember his name tho...', {}],
                                ['...think it was something with Y…', {}]
                            ])                            
                        # print(self.collect_counter)
        elif self.collect_counter >= 3:
            self.ui.cut_scene.createCutScene([
                ['This trip was easier than handling git!', {}],
                ['Who built this prison? A bunch of drunk students?!', {}],
                ['Now I need to find the exit without being raped by aliens...', {}],
                ['...although...heh', {}]
            ])
            self.winning()

    def winning(self):
        pass
