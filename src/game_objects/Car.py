import pygame

class Car():
    def __init__(self, x,y,w,h):
        self.rect = pygame.Rect((x,y),(w,h))
        self.speed = 10
        
    def update(self):
        y = self.rect.y
        y += self.speed
        self.rect.y += self.speed
    