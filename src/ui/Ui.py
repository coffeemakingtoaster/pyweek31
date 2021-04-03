import pygame

from .UiHelper import * 
from .. import config
from .Notification import *
from .Menu import *
from .CutScene import *
from .Hud import *

class Ui:

    def __init__(self, classes):
        self.uiHelper = UiHelper()
        self.notification = Notification(self)
        self.menu = Menu(self, classes)
        self.cut_scene = CutScene(self)
        self.hud = Hud(self, classes)
        self.classes = classes


    def update(self):
        pass

    def draw_ui(self, render):
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



        self.menu.update()
        self.cut_scene.update()
        self.hud.update()

        self.hud.render(render)
        self.cut_scene.render(render)
        self.menu.render(render)
        self.notification.render(render)


    def say(self, message, force_display = False, time = 130):

        self.notification.pushNotification(message, {
            'time': time,
            'color': (255, 255, 255),
            'force_display': force_display
        })