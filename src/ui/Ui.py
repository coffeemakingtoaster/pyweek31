import pygame

from .UiHelper import * 
from ..config import *
from .Notification import *
from .Menu import *

class Ui:

    def __init__(self, classes):
        self.uiHelper = UiHelper()
        self.notification = Notification(self)
        self.menu = Menu(self, classes)
        self.say('Ui loaded!')


    def update(self):
        pass

    def draw_ui(self, render):

        self.notification.render(render)
        self.menu.update()
        self.menu.render(render)

        start_time = pygame.time.get_ticks()
        self.uiHelper.createText(str(start_time/1000), {
            'font': self.uiHelper.fonts['text'],
            'render': render,
            'x': WINDOW_WIDHT - 100,
            'y': 50,
            'color': (255, 255, 255)
        })

        self.uiHelper.createRectangle({
            'x': 20,
            'y': 20,
            'width': 100,
            'height': 100,
            'color': (255, 0, 0),
            'render': render
        })

    def say(self, message):
        self.notification.pushNotification(message, {
            'time': 600,
            'color': (255, 255, 255)
        })
        

