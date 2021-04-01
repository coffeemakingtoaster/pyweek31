from ..superclasses import Actor
from .helper.Section import *
from .helper.Point import *
import math

class Guard(Actor.Actor):

    def __init__(self,pos,walls):
        super().__init__()

        self.pos = pos
        self.goalPos = Point(300,300)
        self.walls = walls

        self.rotation = 0
        self.intersections = []

    def update(self):

        for x in range(-60,61,30):
            self.intersections.append(self.raycast(x,400,self.walls))
        pass

    def raycast(self, degree, length, walls):



        end = Point(self.pos.x+self.addAngleToVector(degree,Point(self.goalPos.x-self.pos.x,self.goalPos.y-self.pos.y)).x,self.pos.y+self.addAngleToVector(degree,Point(self.goalPos.x-self.pos.x,self.goalPos.y-self.pos.y)).y)


        ray = Section(Point(self.pos.x,self.pos.y),Point(end.x,end.y))
        m = (ray.endPoint.x-ray.startPoint.x)/(ray.endPoint.y-ray.startPoint.y)
        intersections = []
        intersections.append((length,end))
        for wall in walls:
            m_wall = (wall.endPoint.x -wall.startPoint.x)/(wall.endPoint.y -wall.startPoint.y)
            intersection = Point((-ray.startPoint.y+wall.startPoint.y)/(m-m_wall),(ray.startPoint.y+m*(-ray.startPoint.y+wall.startPoint.y)/(m-m_wall)))
            distance = distance(ray.startPoint,ray.endPoint)
            if distance > length:
                intersection = Point(999,999)
            if not (wall.startPoint.x < intersection.x) and (wall.endPoint > intersection.x):
                intersection = Point(999,999)
            tup = (distance,intersection)
            intersections.append(tup)
        intersections.sort(key=lambda tup: tup[1])
        return Point(intersections[0][1].x,intersections[0][1].y)









    def move(self):
        #movement
        return goalPos

    def distance(a,b):
        return sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

    def addAngleToVector(self,angle,vector):
        return  Point((math.cos(math.radians(angle))*vector.x - math.sin(math.radians(angle))*vector.y),(math.sin(math.radians(angle))*vector.x +math.cos(math.radians(angle))*vector.y));

    def normVector(self,x,y):
        if x == 0 and y == 0:
            return Point(0,0)
        normFactor = math.sqrt(1/(x*x+y*y))
        return Point(normFactor*x,normFactor*y)

