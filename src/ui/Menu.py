from ..config import *
import pygame

class Menu():

    def __init__(self, ui, classes):
        self.menu = {}
        self.current_menu = 'Main Menu'
        self.current_option = 0
        self.ui = ui
        self.is_controlling = False
        self.is_waiting = False
        self.time_when_control = None
        self.time_wait = 100
        self.time_wait_use = 150
        self.time_wait_back = 150
        self.time_wait_open = 300
        self.open = False
        self.optionsToDisplay = 6

        # Create a menu
        # self.add_menu(<menu_name>, <[optional]parent_menu_name>, <[optional]custom_display_name>)
        # <menu_name>: Menu name
        # <parent_menu_name>: Menu name of the parent menu (if you go back with ESC)
        # <custom_display_name>: Custom message if the Menu name is duplicated

        # Add option to a menu
        # self.add_option(<menu_name>, <option_name>, lambda: <callback_when_use>)
        # <menu_name>: Menu name of the menu where the option should be added
        # <option_name>: Display text of this option 
        # <callback_when_use>: function to call when the user presses this option

        # Link to another menu
        # self.add_option(<menu_name>, <option_name>, lambda: self.set_menu(<menu_name_you_want_to_go>))
        # <menu_name_you_want_to_go>: The menu name where you want to go


        self.add_menu('Main Menu') 
        for x in range(100):
            self.add_option("Main Menu", "opt " + str(x), lambda: print("opt"))

        #self.add_option("Main Menu", "Options", lambda: self.set_menu('Options'))
        #self.add_option("Main Menu", "End", lambda: pygame.quit())
        
        self.add_menu('Options', 'Main Menu')
        self.add_option("Options", "Dev play sounds", lambda: self.set_menu("Dev Play Sounds"))
        for x in range(100):
            self.add_option("Options", "opt " + str(x), lambda: print("opt"))
 
        self.add_menu('Dev Play Sounds', 'Options')
        self.add_option("Dev Play Sounds", "Play Dog Sound", lambda: classes['soundHelper'].play_sfx(classes['assets']['sounds']['bark'], 0))
        #print(self.menu)

        self.ui.say('Press ESC to open menu')


    def add_menu(self, name, parent = None, custom_display_name = None):
        if custom_display_name is None:
            custom_display_name = name

        self.menu[name] = {
            'options': [],
            'scroller': 0,
            'parent': parent,
            'name': custom_display_name
        }

    def add_option(self, menu_name, option_name, callback):
        if menu_name not in self.menu:
            # print(menu_name, " doesn't exist")
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
            if self.open is not True and pygame.key.get_pressed()[pygame.K_ESCAPE]:
                self.is_waiting = True
                self.time_when_control = pygame.time.get_ticks() + self.time_wait_open
                self.open = True
                self.ui.say('###MENU CONTROLS###')
                self.ui.say('Move up and down with ARROW KEYS')
                self.ui.say('Press ENTER to select an option')
                self.ui.say('Press ESC to go back')
            elif self.open is True and (pygame.key.get_pressed()[pygame.K_UP] == True or pygame.key.get_pressed()[pygame.K_DOWN] == True or pygame.key.get_pressed()[pygame.K_RETURN] == True or pygame.key.get_pressed()[pygame.K_ESCAPE] == True):
                self.is_waiting = True
                self.is_controlling = True
                if pygame.key.get_pressed()[pygame.K_UP] == True:
                    self.time_when_control = pygame.time.get_ticks() + self.time_wait
                    if self.current_option < 1:
                        self.current_option += len(self.menu[self.current_menu]['options']) - 1
                    else:
                        self.current_option -= 1 
                    self.menu[self.current_menu]['scroller'] = self.current_option
                elif pygame.key.get_pressed()[pygame.K_DOWN] == True:
                    self.time_when_control = pygame.time.get_ticks() + self.time_wait
                    if self.current_option > len(self.menu[self.current_menu]['options']) - 2:
                       self.current_option = 0
                    else:
                        self.current_option += 1
                    self.menu[self.current_menu]['scroller'] = self.current_option
                elif pygame.key.get_pressed()[pygame.K_RETURN] == True:
                    self.menu[self.current_menu]['options'][self.current_option]['callback']()
                    self.time_when_control = pygame.time.get_ticks() + self.time_wait_use
                elif self.menu[self.current_menu]['parent'] == None and pygame.key.get_pressed()[pygame.K_ESCAPE] == True:
                    self.is_waiting = True
                    self.time_when_control = pygame.time.get_ticks() + self.time_wait_open
                    self.open = False
                elif pygame.key.get_pressed()[pygame.K_ESCAPE] == True:
                    self.time_when_control = pygame.time.get_ticks() + self.time_wait_back
                    if self.menu[self.current_menu]['parent'] is not None:
                        self.set_menu(self.menu[self.current_menu]['parent'])

                #print("Current option is: ", self.current_option, " ", pygame.time.get_ticks())
                self.is_controlling = False

    def render(self, render):
        if self.open is False:
            return

        self.ui.uiHelper.createRectangle({
            'x': 0,
            'y': 0,
            'width': WINDOW_WIDHT / 3,
            'height': WINDOW_HEIGHT,
            'color': (91, 91, 91),
            'render': render
        })

        start_menu_options_x = WINDOW_WIDHT/30


        self.ui.uiHelper.createText(self.menu[self.current_menu]['name'], {
            'font': self.ui.uiHelper.fonts['headline']['font'],
            'render': render,
            'x': start_menu_options_x,
            'y': 200 - self.ui.uiHelper.fonts['headline']['font_height'],
            'color': (220, 220, 220)
        })

        #self.ui.uiHelper.createRectangle({
        #    'x': start_menu_options_x,
        #    'y': 300  + self.ui.uiHelper.fonts['text']['font_height'] * self.current_option,
        #    'width': 100,
        #    'height': self.ui.uiHelper.fonts['text']['font_height'],
        #    'color': (255, 0, 0),
        #    'render': render
        #})
        index = 0
        for option in self.menu[self.current_menu]['options']:
            if index is self.current_option:
                currentColor = (220, 220, 220)
            else:
                currentColor = (158, 158, 158)

            self.ui.uiHelper.createText(option['name'], {
                'font': self.ui.uiHelper.fonts['h2']['font'],
                'render': render,
                'x': start_menu_options_x,
                'y': 300 + self.ui.uiHelper.fonts['h2']['font_height'] * index,
                'color': currentColor
            })


            index += 1