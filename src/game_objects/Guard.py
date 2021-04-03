from ..superclasses import Actor
from .helper.Section import *
from .helper.Point import *
from ..config import *
from pygame.math import Vector2
import math
import pygame

class Guard(Actor.Actor):

    def __init__(self, pos, walls, player, waypoints, props, game_state):
        super().__init__()

        # verify props
        if props['speed'] == "default":
            props['speed'] = 2

        if props['type'] == "default":
            props['type'] = 'line'

        self.guard_speed = props['speed']

        #print(pos, waypoints)
        self.pos = Point.to_our_point(pos)
        self.goalPos = Point(0, 0)

        self.hitbox = pygame.Rect(self.pos.x, self.pos.y, 50, 50)

        self.logic = props['logic']
        self.goalPos = waypoints[0]
        self.goalPosVector = Point(0,0)
        self.walls = walls
        self.player = player

        self.waypoints = []
        self.original_waypoints = []
        self.guard_waypoints_logic = props['type'] # line or circle (line moves 1 -> 2 -> 3 -> 2 -> 1 ...) | (circle moves 1 -> 2 -> 3 -> 1 -> 2 -> 3 ...)
        self.guard_waypoint_direction_back = True

        self.waypoint_variance = 3
        for waypoint in waypoints:
            self.waypoints.append(Point.to_our_point(waypoint))
            self.original_waypoints.append(Point.to_our_point(waypoint))

        self.current_waypoint = 0
        self.is_moving = True
        self.off_patrol_position = Point(-1, -1)
        self.former_current_waypoint = self.current_waypoint


        self.rotation = 0
        self.intersections = []
        
        self.ray_length = GUARD_SIGHT_LENGTH

        self.game_state = game_state

    def update(self, walls):
        self.walls = walls
        self.move(self.goalPos, self.waypoints)

        print(len(self.waypoints), "current_waypoint: " , self.current_waypoint)
        # for x in range(len(waypoints)- 1):
            # if self.current_waypoint > len(waypoints):
                # self.current_waypoint -= 1
                
        if self.current_waypoint < 0 or self.current_waypoint > len(self.waypoints) - 1:
            self.current_waypoint = 0
        self.goalPos = self.waypoints[self.current_waypoint]
        normed_move_vec = self.normVector(self.goalPos.x-self.pos.x,self.goalPos.y-self.pos.y, self.guard_speed)
        self.rotation = self.vector_to_angle(normed_move_vec.x,normed_move_vec.y)
        
        # blocks player for donut item
        if self.is_moving == True:
            self.pos.x += normed_move_vec.x
            self.pos.y += normed_move_vec.y
            self.hitbox.x = self.pos.x
            self.hitbox.y = self.pos.y

        #rad_rot = self.angle_to_rad(self.rotation)
        #self.goalPosVector = Point(-math.sin(rad_rot),-math.cos(rad_rot))

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

            for x in range(-40,41,15):
                self.intersections.append(self.raycast(x, self.ray_length, self.walls, player_sections))
        pass

    def raycast(self, degree, length, walls, player_sections):

        #end = Point(self.pos.x+self.addAngleToVector(degree,
        #      Point(self.goalPos.x-self.pos.x,self.goalPos.y-self.pos.y)).x,
        #      self.pos.y+self.addAngleToVector(degree,
        #      Point(self.goalPos.x-self.pos.x,self.goalPos.y-self.pos.y)).y)

        normed_goalPos = self.addAngleToVector(degree,self.normVector(self.goalPos.x-self.pos.x,self.goalPos.y-self.pos.y,length))



        end = Point(self.pos.x+normed_goalPos.x,self.pos.y+normed_goalPos.y)



        ray = Section(self.pos, end)
        if (ray.endPoint.x-ray.startPoint.x) == 0:
            ray.endPoint.x += 0.01
        m = (ray.endPoint.y-ray.startPoint.y)/(ray.endPoint.x-ray.startPoint.x)
        if m == 0:
            m = 0.01

        #free society
        intersections = [(length, end,"none")]
        y_axis_section = ray.startPoint.y - m * ray.startPoint.x
        for wall in walls:

            if wall.endPoint.x == wall.startPoint.x:
                intersection = Point(wall.endPoint.x, y_axis_section+m*wall.endPoint.x)
                if wall.endPoint.y > intersection.y > wall.startPoint.y and min(ray.startPoint.y,ray.endPoint.y) < intersection.y < max(ray.startPoint.y,ray.endPoint.y):
                    distance = self.distance(self.pos, intersection)
                    intersections.append((distance, intersection,"wall"))
            if wall.endPoint.y == wall.startPoint.y:
                intersection = Point((wall.endPoint.y-y_axis_section)/m,wall.startPoint.y)
                if wall.endPoint.x > intersection.x > wall.startPoint.x and min(ray.startPoint.x,ray.endPoint.x) < intersection.x < max(ray.startPoint.x,ray.endPoint.x):
                    distance = self.distance(self.pos,intersection)
                    intersections.append((distance,intersection,"wall"))

        if not self.player.is_hidden:
            for section in player_sections:
                if section.endPoint.x == section.startPoint.x:
                    intersection = Point(section.endPoint.x, y_axis_section + m * section.endPoint.x)
                    if section.endPoint.y > intersection.y > section.startPoint.y and min(ray.startPoint.y,ray.endPoint.y) < intersection.y < max(ray.startPoint.y,ray.endPoint.y):
                        distance = self.distance(self.pos, intersection)
                        intersections.append((distance, intersection, "player"))
                if section.endPoint.y == section.startPoint.y:
                    intersection = Point((section.endPoint.y - y_axis_section) / m, section.startPoint.y)
                    if section.endPoint.x > intersection.x > section.startPoint.x and min(ray.startPoint.x,ray.endPoint.x) < intersection.x < max(ray.startPoint.x,ray.endPoint.x):
                        distance = self.distance(self.pos, intersection)
                        intersections.append((distance, intersection, "player"))





        intersections.sort(key=lambda tup: tup[0])
        for tuple in intersections:
            correct_intersection = intersections[0]
            if correct_intersection[2] == "player":
                self.game_state.set_game_state("over")
            return Point(correct_intersection[1].x,correct_intersection[1].y)

    def check_vision(self):
        return True

    def move(self,goalPos,waypoints):
        if self.logic.coin.x - 10 <= self.pos.x <= self.logic.coin.x + 10 and self.logic.coin.y - 10 <= self.pos.y <= self.logic.coin.y + 10:
            self.logic.coin.is_active = False
            self.logic.coin.is_rendered = False
            print("reached coin")
            
        if self.logic.coin.is_active == False and self.off_patrol_position.x - 10 <= self.pos.x <= self.off_patrol_position.x + 10 and self.off_patrol_position.y - 10 <= self.pos.y <= self.off_patrol_position.y + 10:
            self.waypoints = self.original_waypoints.copy()
            self.off_patrol_position = Point(-1, -1)
            self.current_waypoint = self.former_current_waypoint
            print("reached off patrol point", len(self.waypoints), len(self.original_waypoints))
            
        elif goalPos.x + self.waypoint_variance > self.pos.x > goalPos.x - self.waypoint_variance and goalPos.y + self.waypoint_variance > self.pos.y > goalPos.y - self.waypoint_variance:
            if self.guard_waypoints_logic == 'circle':
                if self.current_waypoint >= len(waypoints) - 1:
                    self.current_waypoint = 0
                    return
                self.current_waypoint += 1
            elif self.guard_waypoints_logic == 'line':
                if self.current_waypoint >= len(waypoints) - 1 or self.current_waypoint == 0:
                    self.guard_waypoint_direction_back = not self.guard_waypoint_direction_back
                if self.guard_waypoint_direction_back: 
                    self.current_waypoint -= 1
                else:
                    self.current_waypoint += 1
            #print("self.current_waypoint", self.current_waypoint, "self.guard_waypoints_logic", self.guard_waypoints_logic)

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

    def vector_to_angle(self,x,y):
        return pygame.math.Vector2(x, y).angle_to((0, -1))

    def check_vision_to_point(self, point):


        ray = Section(self.pos,point)
        m = (ray.endPoint.y - ray.startPoint.y) / (ray.endPoint.x - ray.startPoint.x)
        y_axis_section = ray.startPoint.y - m * ray.startPoint.x


        for wall in self.walls:

            if wall.endPoint.x == wall.startPoint.x:
                intersection = Point(wall.endPoint.x, y_axis_section+m*wall.endPoint.x)
                if wall.endPoint.y > intersection.y > wall.startPoint.y and min(ray.startPoint.y,ray.endPoint.y) < intersection.y < max(ray.startPoint.y,ray.endPoint.y):
                    return False

            if wall.endPoint.y == wall.startPoint.y:
                intersection = Point((wall.endPoint.y-y_axis_section)/m,wall.startPoint.y)
                if wall.endPoint.x > intersection.x > wall.startPoint.x and min(ray.startPoint.x,ray.endPoint.x) < intersection.x < max(ray.startPoint.x,ray.endPoint.x):
                    return False
        return True
