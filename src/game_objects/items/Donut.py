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
        print('Donut trap is placed at ' + str(x) + ' ' + str(y))
        width = 50
        height = 50
        self.placed_traps.append(pygame.Rect(x, y, width, height))
        self.is_placed = True
        
    def snap_trap(self):
        if self.is_placed:
            for guard in self.logic.enemies:
                for trap in self.placed_traps:
                    if pygame.Rect.colliderect(trap, guard.hitbox):
                        print('A guard has stepped into the trap.')
                        self.logic.soundHelper.play_tickless_sfx(self.logic.assets["sounds"]["donut_pickup"],0)
                        guard.is_moving = False
                        threading.Timer(self.duration, lambda guard = guard: self.digest(guard)).start()  
                        self.placed_traps.remove(trap)
    
    def digest(self, guard):
        print('A guard has freed himself from a trap.')
        guard.is_moving = True