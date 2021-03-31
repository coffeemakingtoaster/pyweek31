from ..superclasses import Actor
from .helper.Section import *
from .helper.Point import *
import math

class Guard(Actor.Actor):

    def __init__(self,pos):
        super().__init__()

        self.pos = pos
        self.goalPos = pos

        self.rotation = 0


    def update(self):
        pass

    def raycast(self, degree, length, walls):

        end = Point(200,200)
        ray = Section((self.pos.x,self.pos.y),(end.x,end.y))
        m = (ray.endPoint[0]-ray.startPoint[0])/(ray.endPoint[1]-ray.startPoint[1])
        intersections = []
        for wall in walls:
            m_wall = (wall.endPoint[0]-wall.startPoint[0])/(wall.endPoint[1]-wall.startPoint[1])
            intersection = Point((-ray.startPoint[1]+wall.startPoint[1])/(m-m_wall),(ray.startPoint[1]+m*(-ray.startPoint[1]+wall.startPoint[1])/(m-m_wall)))
            distance = distance(ray.startPoint,ray.endPoint)
            if distance > length:
                intersection = Point(999,999)
            if not (wall.startPoint.x < intersection.x) and (wall.endPoint > intersection.x):
                intersection = Point(999,999)
            tup = (distance,intersection)
            intersections.append(tup)
        intersections.sort(key=lambda tup: tup[1])
        return Point(intersections[0][1],intersections[0][2])









    def move(self):
        #movement
        return goalPos

    def distance(a,b):
        return sqrt((a.x - b.x)**2 + (a.y - b.y)**2)
