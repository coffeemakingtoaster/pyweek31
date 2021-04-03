from ...config import *
from ...superclasses import Item
import time, threading
import pygame

class Donut(Item.Item):
    def __init__(self, logic):
        super().__init__('donut', logic)
        self.duration = ITEM_DONUT_DURATION
        self.is_placed = False
        self.placed_traps = []
        
    def place(self, x, y):
        width = 50
        height = 50
        self.placed_traps.append(pygame.Rect(x, y, width, height))
        self.is_placed = True
        
    def snap_trap(self):
        if self.is_placed:
            for guard in self.logic.enemies:
                for trap in self.placed_traps:
                    if pygame.Rect.colliderect(trap, guard.hitbox):
                        self.logic.soundHelper.play_tickless_sfx(self.logic.assets["sounds"]["donut_pickup"],0)
                        guard.is_moving = False
                        threading.Timer(self.duration, lambda guard = guard: self.digest(guard)).start()  
                        self.placed_traps.remove(trap)
    
    def digest(self, guard):
        guard.is_moving = True