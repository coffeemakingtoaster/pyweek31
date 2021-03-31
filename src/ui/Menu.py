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

        # Create a menu
        # self.add_menu(<menu_name>, <parent_menu_name>)
        # <menu_name>: Menu name (string, key, not human readable)
        # <parent_menu_name>: Menu name (string, key, not human readable) of the parent menu (if you go back with ESC)

        # Add option to a menu
        # self.add_option(<menu_name>, <option_name>, lambda: <callback_when_use>)
        # <menu_name>: Menu name of the menu where the option should be added
        # <option_name>: Display text of this option 
        # <callback_when_use>: function to call when the user presses this option

        # Link to another menu
        # self.add_option(<menu_name>, <option_name>, lambda: self.set_menu(<menu_name_you_want_to_go>))
        # <menu_name_you_want_to_go>: The menu name (key) where you want to go


        self.add_menu('main') 
        self.add_option("main", "Options", lambda: self.set_menu('options'))
        self.add_option("main", "End", lambda: print('end'))
        
        self.add_menu('options', 'main')
        self.add_option("options", "Dev play sounds", lambda: self.set_menu("options_sounds"))
        for x in range(100):
            self.add_option("options", "opt " + str(x), lambda: print("opt"))
 
        self.add_menu('options_sounds', 'options')
        self.add_option("options_sounds", "Play Dog Sound", lambda: classes['soundHelper'].play_sfx(classes['assets']['sounds']['bark'], 0))

        ui.say('###MENU CONTROLS###')
        ui.say('Move up and down with ARROW KEYS')
        ui.say('Press ENTER to select an option')
        ui.say('Press ESC to go back')

        print(self.menu)

    def add_menu(self, name, parent = None):
        self.menu[name] = {
            'options': [],
            'scroller': 0,
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

    def set_menu(self, menu_name, current_option = None):
        if menu_name not in self.menu:
            print(menu_name, " doesn't exist")
            return

        if current_option is None:
            current_option = self.menu[menu_name]['scroller']

        if current_option > len(self.menu[menu_name]['options']) - 1:
            current_option = 0
            print("The selected option is not there. Seems like something isn't working here. To bad!")
        self.current_menu = menu_name
        
        self.current_option = current_option

    def update(self):
        if self.time_when_control is not None and pygame.time.get_ticks() > self.time_when_control:
            self.is_waiting = False
        if self.is_controlling is False and self.is_waiting is False:
            if pygame.key.get_pressed()[pygame.K_UP] == True or pygame.key.get_pressed()[pygame.K_DOWN] == True or pygame.key.get_pressed()[pygame.K_RETURN] == True or pygame.key.get_pressed()[pygame.K_ESCAPE] == True:
                self.time_when_control = pygame.time.get_ticks() + self.time_wait
                self.is_waiting = True
                self.is_controlling = True
                if pygame.key.get_pressed()[pygame.K_UP] == True:
                    if self.current_option < 1:
                        self.current_option += len(self.menu[self.current_menu]['options']) - 1
                    else:
                        self.current_option -= 1 
                    self.menu[self.current_menu]['scroller'] = self.current_option
                elif pygame.key.get_pressed()[pygame.K_DOWN] == True:
                    if self.current_option > len(self.menu[self.current_menu]['options']) - 2:
                       self.current_option = 0
                    else:
                        self.current_option += 1
                    self.menu[self.current_menu]['scroller'] = self.current_option
                elif pygame.key.get_pressed()[pygame.K_RETURN] == True:
                    self.menu[self.current_menu]['options'][self.current_option]['callback']()
                elif pygame.key.get_pressed()[pygame.K_ESCAPE] == True:
                    if self.menu[self.current_menu]['parent'] is not None:
                        self.set_menu(self.menu[self.current_menu]['parent'])

                print("Current option is: ", self.current_option, " ", pygame.time.get_ticks())
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