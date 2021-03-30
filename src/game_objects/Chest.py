from ..superclasses import InteractiveObject

class Chest(InteractiveObject.InteractiveObject):

    def __init__(self):
        super().__init__()
        self.x = 100
        self.y = 100

    def update(self):
        pass
