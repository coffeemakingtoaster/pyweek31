from random import choices

from ..superclasses.InteractiveObject import *
from .. import config

class Chest(InteractiveObject):

    def __init__(self):
        super().__init__()
        self.x = 100
        self.y = 100
        self.is_empty = False
        self.possible_items = ["coin","donut","coffee","jammer"]
        self.probabilities = [config.ITEM_COIN_CHANCE,config.ITEM_DONUT_CHANCE,config.ITEM_COFFEE_CHANCE,config.ITEM_JAMMER_CHANCE]

    def update(self):
        pass

    def open(self):
        #self.is_empty = True
        return choices(population=self.possible_items,weights=self.probabilities)[0]
