import random
import pygame

class Mice():

    def __init__(self):
        self.pos_x = 0
        self.pos_y = 0
        self.speed = 100
        self.moving = False
        self.destination_x = 0
        self.destination_y = 0

    moving_areas = [{"x": (986, 1466), "y":(543, 663)}, {"x":(376, 1715), "y":(1373, 1472)}, {"x":(378, 476), "y":(1579, 2273)}, {"x":(3030, 3511), "y":(1932, 2073)}, {"x":(4291, 6021), "y":(2173, 2223)}]
    mice_start_surface = pygame.image.load('data/assets/mapsprite/mouse1.png')
    mice_moved_surface = pygame.image.load('data/assets/mapsprite/mouse2.png')

    def create(self, mouse):
        mouse = []
        for i in range(3):
            index = random.choice(self.moving_areas)
            x1, x2 = index["x"]
            self.pos_x = random.randrange(x1,x2)
            y1, y2 = index["y"]
            self.pos_y = random.randrange(y1,y2)
            self.destination_x = random.randrange(x1,x2)
            self.destination_y = random.randrange(y1,y2)
            mouse[i].append({"x": self.pos_x, "y": self.pos_y, "dest_x": self.destination_x, "dest_y": self.destination_y})
            return mouse

    def moving_animation(self):
        pass

    def update(self, pos_x, pos_y, destination_x, destination_y):
        if not self.moving:
            self.moving = True
            print("Mouse", self.pos_x, self.pos_y, self.destination_x, self.destination_y)
            if self.pos_x != self.destination_x or self.pos_y != self.destination_y:
                if self.pos_x == self.destination_x:
                        self.pos_y += self.speed
                if self.pos_x != self.destination_x:
                    if self.pos_y == self.destination_y:
                        self.pos_x += self.speed
                    elif self.pos_y != self.destination_y:
                        self.pos_x += self.speed
                        self.pos_y += self.speed
            self.moving = False
            print("Mouse", self.pos_x, self.pos_y, self.destination_x, self.destination_y)




