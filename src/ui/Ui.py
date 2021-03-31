import pygame

from .UiHelper import * 
from .. import config
from .Notification import *
from .Menu import *

class Ui:

    def __init__(self, classes):
        self.uiHelper = UiHelper()
        self.notification = Notification(self)
        self.menu = Menu(self, classes)
        self.classes = classes
        self.say('Ui loaded!')


    def update(self):
        pass

    def draw_ui(self, render):

        self.notification.render(render)
        self.menu.update()
        self.menu.render(render)

        start_time = pygame.time.get_ticks()
        print(str(self.formatTime(start_time)[0]))
        self.uiHelper.createText(str(self.formatTime(start_time)[0]) + ":" + str(self.formatTime(start_time)[1]), {
            'font': self.uiHelper.fonts['text'],
            'render': render,
            'x': WINDOW_WIDHT - 200,
            'y': 50,
            'color': (255, 255, 255)
        })

        """
        self.uiHelper.createRectangle({
            'x': 20,
            'y': 20,
            'width': 100,
            'height': 100,
            'color': (255, 0, 0),
            'render': render
        })
        """
        self.uiHelper.createSprite({
            'x': 10,
            'y': 20,
            'texture' : self.classes['assets']['textures']['hud'][0],
            'render' : render
        })

        self.uiHelper.createSprite({
            'x': 26,
            'y': 20,
            'texture' : self.classes['assets']['textures']['hud'][1],
            'render' : render
        })

        self.uiHelper.createSprite({
            'x': 42,
            'y': 20,
            'texture' : self.classes['assets']['textures']['hud'][2],
            'render' : render
        })
        

    def say(self, message):
        self.notification.pushNotification(message, {
            'time': 600,
            'color': (255, 255, 255)
        })

    def formatTime(self, time):
        timeArray = []

        #get seconds
        total_seconds = time / 1000

        #get minutes
        minutes = int(total_seconds // 60)
        if minutes < 10:
            minutes = str(0) + str(minutes)
        timeArray.append(minutes)

        #get rest seconds
        rest_seconds = round(total_seconds % 60, 2)
        if rest_seconds < 10:
            rest_seconds = str(0) + str(rest_seconds)

        timeArray.append(rest_seconds)
        

        return timeArray
