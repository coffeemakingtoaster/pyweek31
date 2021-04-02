import pygame

from ..config import *

class CutScene():

    def __init__(self, ui):
        self.uiHelper = ui.uiHelper
        self.ui = ui
        self.cut_scenes = []
        self.blackbar_height = 75
        self.blackbar_color = (0, 0, 0)
        self.is_active = False

        self.time_for_next_click = 0
        self.time_wait = 1000

    # cut_scene.createCutScene([<message>, {'time': <time>, 'color': <color>}])
    # <message>: text to display
    #
    # optional (props):
    # <time>: time to wait till you can press space
    # <color>: color of your text
    # WARNING: props must be at least an empty object (if someone knows how to fix that: DO it! )

    def createCutScene(self, messages):
        self.is_active = True

        if 'time' in messages[0][1]:
            self.time_for_next_click = pygame.time.get_ticks() + messages[0][1]['time']
        else:
            self.time_for_next_click = pygame.time.get_ticks() + self.time_wait
        for message, props in messages:
            self.pushCutScene(message, props)

    def pushCutScene(self, text, props):
        if 'color' not in props:
            props['color'] = (255, 255, 255)

        if 'time' not in props:
            props['time'] = self.time_wait

        self.cut_scenes.append({
            'message': text,
            'color': props['color'],
            'time': props['time']
        })

        #print(text, props)

        
    def update(self):
        if self.is_active is not True:
            return

        if pygame.key.get_pressed()[pygame.K_SPACE] and pygame.time.get_ticks() > self.time_for_next_click and not self.ui.menu.open:
            if len(self.cut_scenes) > 1 and 'time' in self.cut_scenes[0 + 1]:
                self.time_for_next_click = pygame.time.get_ticks() + self.cut_scenes[0 + 1]['time']
                #print(self.cut_scenes[0 + 1]['time']) #time for the next frame
            else:
                self.time_for_next_click = pygame.time.get_ticks() + self.time_wait
            self.cut_scenes.pop(0)

    def render(self, render):
        if len(self.cut_scenes) == 0:
            self.is_active = False

        if self.is_active is not True:
            return
        
        self.render_blackbars(render)
        self.render_text(render)
        self.render_help_text(render)
    
    def render_help_text(self, render):
        if pygame.time.get_ticks() > self.time_for_next_click:
            self.uiHelper.createText('Press SPACE ...', {
                'font': self.uiHelper.fonts['text']['font'],
                'render': render,
                'x': WINDOW_WIDHT - 200,
                'y': WINDOW_HEIGHT - self.blackbar_height - 30,
                'color': (255, 255, 255)
            })

    def render_text(self, render):
        self.uiHelper.createText(self.cut_scenes[0]['message'], {
            'font': self.uiHelper.fonts['text']['font'],
            'render': render,
            'x': 40,
            'y': WINDOW_HEIGHT - self.blackbar_height / 2 - self.uiHelper.fonts['text']['font_height'] / 2,
            'color': self.cut_scenes[0]['color']
        })

    def render_blackbars(self, render):
        self.uiHelper.createRectangle({
            'x': 0,
            'y': 0,
            'width': WINDOW_WIDHT,
            'height': self.blackbar_height,
            'color': self.blackbar_color,
            'render': render
        })
        self.uiHelper.createRectangle({
            'x': 0,
            'y': WINDOW_HEIGHT - self.blackbar_height,
            'width': WINDOW_WIDHT,
            'height': self.blackbar_height,
            'color': self.blackbar_color,
            'render': render
        })