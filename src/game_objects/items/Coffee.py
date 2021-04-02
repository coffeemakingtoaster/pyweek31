from ...config import *
from ...superclasses import Item
import time, threading

class Coffee(Item.Item):
    def __init__(self, logic):
        super().__init__('coffee', logic)
        self.boosted_speed = ITEM_COFFEE_SPEED
        self.duration = ITEM_COFFEE_DURATION
        
    def drink(self):
        self.logic.player.speed = self.boosted_speed
        threading.Timer(self.duration, self.digest).start()
        
    def digest(self):
        print("Now using {}".format('coffee')) 
        self.logic.player.speed = PLAYER_SPEED