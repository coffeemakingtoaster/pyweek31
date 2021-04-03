import random
import pygame

class Mouse():
    def __init__(self):
        self.moving_areas = [
            {"x": (986, 1466), "y":(543, 663)},
            {"x": (376, 1715), "y":(1373, 1472)}, 
            {"x": (378, 476), "y":(1579, 2273)}, 
            {"x": (3030, 3511), "y":(1932, 2073)}, 
            {"x": (4291, 6021), "y":(2173, 2223)},
            {"x": (1000, 1000), "y":(1000, 1500)}
        ]
        self.area_index = random.randint(0,len(self.moving_areas)-1)
        target = self.moving_areas[self.area_index]      
        x1, x2 = target["x"]
        y1, y2 = target["y"]
        self.target = (x2,y2)
        self.start = (x1,y1)
        self.x = x1
        self.y = y1
        self.speed = 2
        self.rotation = 0
    
    def calculate_new_waypoint(self):
        x_boundry1, x_boundry2 = self.moving_areas[self.area_index]["x"]
        y_boundry1, y_boundry2 = self.moving_areas[self.area_index]["y"]
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




