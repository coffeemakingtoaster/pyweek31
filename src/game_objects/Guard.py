from ..superclasses import Actor

class Guard(Actor.Actor):

    def __init__(self):
        super().__init__()
        self.x = 200
        self.y = 200
        self.rotation = 0

    def update(self):
        pass
