from ..superclasses import Actor
from .helper.Section import *
from .helper.Point import *
from pygame.math import Vector2
import math
import pygame

class Guard(Actor.Actor):

    def __init__(self,pos,walls,player):
        super().__init__()

        self.pos = pos
        self.goalPos = Point(0 ,0)
        self.walls = walls
        self.player = player
        
        self.hitbox = pygame.Rect((0,0),(50,50))

        self.rotation = 0
        self.intersections = []
    
    def update(self,walls):
        self.rotation += 5
        rad_rot = self.angle_to_rad(self.rotation)
        self.goalPos = Point(-math.sin(rad_rot),-math.cos(rad_rot))

        player_sections = [Section(Point(self.player.player_hitbox.x ,self.player.player_hitbox.y) ,
                                   Point(self.player.player_hitbox.x + self.player.player_hitbox.width ,self.player.player_hitbox.y)),
                           Section(Point(self.player.player_hitbox.x ,self.player.player_hitbox.y) ,
                                   Point(self.player.player_hitbox.x ,self.player.player_hitbox.y + self.player.player_hitbox.height)),
                           Section(Point(self.player.player_hitbox.x ,self.player.player_hitbox.y + self.player.player_hitbox.height),
                                   Point(self.player.player_hitbox.x + self.player.player_hitbox.width ,self.player.player_hitbox.y + self.player.player_hitbox.height)),
                           Section(Point(self.player.player_hitbox.x + self.player.player_hitbox.width ,self.player.player_hitbox.y),
                                   Point(self.player.player_hitbox.x + self.player.player_hitbox.width ,self.player.player_hitbox.y + self.player.player_hitbox.height))]
        self.intersections = []
        if self.distance(self.pos,Point(self.player.x,self.player.y)) < 600:

            for x in range(-40,41,2):
                self.intersections.append(self.raycast(x,200,walls,player_sections))
        pass

    def raycast(self, degree, length, walls, player_sections):

        #end = Point(self.pos.x+self.addAngleToVector(degree,
        #      Point(self.goalPos.x-self.pos.x,self.goalPos.y-self.pos.y)).x,
        #      self.pos.y+self.addAngleToVector(degree,
        #      Point(self.goalPos.x-self.pos.x,self.goalPos.y-self.pos.y)).y)

        normed_goalPos = self.addAngleToVector(degree,self.normVector(self.goalPos.x,self.goalPos.y,length))



        end = Point(self.pos.x+normed_goalPos.x,self.pos.y+normed_goalPos.y)



        ray = Section(self.pos, end)
        if (ray.endPoint.x-ray.startPoint.x) == 0:
            ray.endPoint.x += 0.01
        m = (ray.endPoint.y-ray.startPoint.y)/(ray.endPoint.x-ray.startPoint.x)
        if m == 0:
            m = 0.01

        intersections = [(length, end)]
        y_axis_section = ray.startPoint.y - m * ray.startPoint.x
        for wall in walls:

            if wall.endPoint.x == wall.startPoint.x:
                intersection = Point(wall.endPoint.x, y_axis_section+m*wall.endPoint.x)
                if wall.endPoint.y > intersection.y > wall.startPoint.y and min(ray.startPoint.y,ray.endPoint.y) < intersection.y < max(ray.startPoint.y,ray.endPoint.y):
                    distance = self.distance(self.pos, intersection)
                    intersections.append((distance, intersection))
            if wall.endPoint.y == wall.startPoint.y:
                intersection = Point((wall.endPoint.y-y_axis_section)/m,wall.startPoint.y)
                if wall.endPoint.x > intersection.x > wall.startPoint.x and min(ray.startPoint.x,ray.endPoint.x) < intersection.x < max(ray.startPoint.x,ray.endPoint.x):
                    distance = self.distance(self.pos,intersection)
                    intersections.append((distance,intersection))


        for section in player_sections:
            if section.endPoint.x == section.startPoint.x:
                intersection = Point(section.endPoint.x, y_axis_section + m * section.endPoint.x)
                if section.endPoint.y > intersection.y > section.startPoint.y and min(ray.startPoint.y,ray.endPoint.y) < intersection.y < max(ray.startPoint.y,ray.endPoint.y):
                    distance = self.distance(self.pos, intersection)
                    intersections.append((distance, intersection))
            if section.endPoint.y == section.startPoint.y:
                intersection = Point((section.endPoint.y - y_axis_section) / m, section.startPoint.y)
                if section.endPoint.x > intersection.x > section.startPoint.x and min(ray.startPoint.x,ray.endPoint.x) < intersection.x < max(ray.startPoint.x,ray.endPoint.x):
                    distance = self.distance(self.pos, intersection)
                    intersections.append((distance, intersection))





        intersections.sort(key=lambda tup: tup[0])
        for tuple in intersections:
            correct_intersection = intersections[0]
            return Point(correct_intersection[1].x,correct_intersection[1].y)









    def move(self):

        return goalPos

    def distance(self,a,b):
        return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

    def addAngleToVector(self,angle,vector):
        return  Point((math.cos(math.radians(angle))*vector.x - math.sin(math.radians(angle))*vector.y),
                      (math.sin(math.radians(angle))*vector.x +math.cos(math.radians(angle))*vector.y))

    def normVector(self,x,y,length):
        if x == 0 and y == 0:
            return Point(0,0)
        normFactor = length* math.sqrt(1/(x*x+y*y))
        return Point(normFactor*x,normFactor*y)

    def angle_to_rad(self,angle):
        return angle/180 * math.pi

