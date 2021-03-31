from ..config import *
import pygame

class Menu():

    def __init__(self, ui, classes):
        self.menu = {}
        self.current_menu = 'main'
        self.current_option = 0
        self.font_height = 20
        self.ui = ui
        self.is_controlling = False
        self.is_waiting = False
        self.time_when_control = None
        self.time_wait = 100

        self.add_menu('main')
        self.add_option("main", "Play Dog Sound", lambda: classes['soundHelper'].play_sfx(classes['assets']['sounds']['bark'], 0))
        self.add_option("main", "Options", lambda: print('options'))
        self.add_option("main", "End", lambda: print('end'))

        print(self.menu)

    def add_menu(self, name, parent = None):
        self.menu[name] = {
            'options': [],
            'scroler': 0,
            'parent': parent
        }

    def add_option(self, menu_name, option_name, callback):
        if menu_name not in self.menu:
            print(menu_name, " doesn't exist")
            return
        self.menu[menu_name]['options'].append({
            'name': option_name,
            'callback': callback
        })

    def update(self):
        if self.time_when_control is not None and pygame.time.get_ticks() > self.time_when_control:
            self.is_waiting = False
        if self.is_controlling is False and self.is_waiting is False:
            self.time_when_control = pygame.time.get_ticks() + self.time_wait
            self.is_waiting = True
            self.is_controlling = True
            if pygame.key.get_pressed()[pygame.K_UP] == True:
                if self.current_option < 1:
                    self.current_option += len(self.menu[self.current_menu]['options']) - 1
                else:
                    self.current_option -= 1 
            elif pygame.key.get_pressed()[pygame.K_DOWN] == True:
                if self.current_option > len(self.menu[self.current_menu]['options']) - 2:
                   self.current_option = 0
                else:
                    self.current_option += 1
            elif pygame.key.get_pressed()[pygame.K_RETURN] == True:
                self.menu[self.current_menu]['options'][self.current_option]['callback']()
            print(self.current_option)
            self.is_controlling = False
    def render(self, render):
        self.ui.uiHelper.createRectangle({
            'x': 300,
            'y': 100  + self.font_height * self.current_option,
            'width': 100,
            'height': self.font_height,
            'color': (255, 0, 0),
            'render': render
        })
        index = 0
        for option in self.menu[self.current_menu]['options']:
            
            self.ui.uiHelper.createText(option['name'], {
                'font': self.ui.uiHelper.fonts['text'],
                'render': render,
                'x': 300,
                'y': 100 + self.font_height * index,
                'color': (255, 255, 255)
            })


            index += 1