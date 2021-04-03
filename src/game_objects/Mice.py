import random
import pygame

class Mouse():
    def __init__(self, spot):
        self.moving_area = {"x": (spot.x, spot.x + spot.width), "y":(spot.y, spot.y + spot.height)}
        target = self.moving_area
        x1, x2 = target["x"]
        y1, y2 = target["y"]
        self.target = (x2,y2)
        self.start = (x1,y1)
        self.x = x1
        self.y = y1
        self.speed = 2
        self.rotation = 0
    
    def calculate_new_waypoint(self):
        x_boundry1, x_boundry2 = self.moving_area["x"]
        y_boundry1, y_boundry2 = self.moving_area["y"]
        self.target = (random.randint(x_boundry1,x_boundry2),random.randint(y_boundry1,y_boundry2))
        
     
    def update(self):
        x,y = self.target
        move_vector = pygame.Vector2(x-self.x,y-self.y)
        self.rotation = move_vector.angle_to(pygame.Vector2(0,1))
        if move_vector.length() <= self.speed:
            self.x = x
            self.y = y
            self.calculate_new_waypoint()
        else:
            move_vector.scale_to_length(self.speed)
            self.x += move_vector.x
            self.y += move_vector.y




