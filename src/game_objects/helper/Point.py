from ...config import *


class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point(" + str(self.x) + ", " + str(self.y) + ")"

    def to_our_point(point):
        return Point(point.x * (TILE_SIZE/16), point.y * (TILE_SIZE/16))
