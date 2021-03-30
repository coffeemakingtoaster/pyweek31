from ..superclasses import InteractiveObject

class Door(InteractiveObject.InteractiveObject):

    def __init__(self):
        super().__init__()
        self.is_open = False

    def update(self):
        pass

