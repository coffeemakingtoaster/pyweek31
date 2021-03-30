from ..superclasses.InteractiveObject import *

class Chest(InteractiveObject):

    def __init__(self):
        super().__init__()
        self.x = 100
        self.y = 100
        self.is_empty = False

    def update(self):
        pass
    
    def open(self):
        if self.is_empty:
            return
        self.is_empty = True
        return "dummy"