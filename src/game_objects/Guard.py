from ..superclasses import Actor
from .helper.Section import *
from .helper.Point import *
import math

class Guard(Actor.Actor):

    def __init__(self,pos,walls):
        super().__init__()

        self.pos = pos
        self.goalPos = Point(pos.x+50,pos.y+50)
        self.walls = walls

        self.rotation = 0
        self.intersections = []

    def update(self):

        self.intersections = []
        for x in range(-60,61,999):
            self.intersections.append(self.raycast(x,100,self.walls))
            print("X: ")
            print(self.intersections[-1].x)
        pass

    def raycast(self, degree, length, walls):

        end = Point(self.pos.x+self.addAngleToVector(degree,Point(self.goalPos.x-self.pos.x,self.goalPos.y-self.pos.y)).x,self.pos.y+self.addAngleToVector(degree,Point(self.goalPos.x-self.pos.x,self.goalPos.y-self.pos.y)).y)
        print("Endpoint")
        print(end.x)
        print(end.y)

        ray = Section(self.pos, end)
        m = (ray.endPoint.y-ray.startPoint.y)/(ray.endPoint.x-ray.startPoint.x)
        intersections = []
        intersections.append((length, end))
        for wall in walls:

            if wall.endPoint.x == wall.startPoint.x:
                intersection = Point(wall.endPoint.x,ray.startPoint.y+m*wall.endPoint.x)
                if intersection.y < wall.endPoint.y and intersection.y > wall.startPoint.y:
                    distance = self.distance(self.pos,intersection)
                    intersections.append((distance,intersection))
            if wall.endPoint.y == wall.startPoint.y:
                intersection = Point(((wall.endPoint.y-ray.startPoint.y)/m),wall.endPoint.y)
                if intersection.x < wall.endPoint.x and intersection.x > wall.startPoint.x:
                    distance = self.distance(self.pos,intersection)
                    intersections.append((distance,intersection))


        intersections.sort(key=lambda tup: tup[0])
        for tuple in intersections:
            print("Intersection X: " + str(tuple[1].x) + " Y: " + str(tuple[1].y))
            print(tuple[0])
        correct_intersection = intersections[0]
        return Point(correct_intersection[1].x,correct_intersection[1].y)









    def move(self):
        #movement
        return goalPos

    def distance(self,a,b):
        return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

    def addAngleToVector(self,angle,vector):
        return  Point((math.cos(math.radians(angle))*vector.x - math.sin(math.radians(angle))*vector.y),(math.sin(math.radians(angle))*vector.x +math.cos(math.radians(angle))*vector.y));

    def normVector(self,x,y):
        if x == 0 and y == 0:
            return Point(0,0)
        normFactor = math.sqrt(1/(x*x+y*y))
        return Point(normFactor*x,normFactor*y)

