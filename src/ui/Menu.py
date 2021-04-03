from ..config import *
import pygame

class Menu():

    def __init__(self, ui, classes):
        self.menu = {}
        self.current_menu = 'Pause'
        self.current_option = 0
        self.ui = ui
        self.classes = classes
        self.is_controlling = False
        self.is_waiting = False
        self.time_when_control = None
        self.time_wait = 100
        self.time_wait_use = 150
        self.time_wait_back = 150
        self.time_wait_open = 300
        self.open = False
        self.colors = [
            (255, 0, 5),
            (255, 242, 140),
            (255, 255, 255),
            (158, 158, 158),
            (91, 91, 91),
            (17, 0, 102),
            (144, 203, 251),
            (231, 76, 60),
            (44, 62, 80),
            (0, 0, 0)
        ]
        self.primaryColor =  self.colors[2]
        self.secondaryColor = self.colors[3]
        self.background = self.colors[4]

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


        self.add_menu('Pause') 
        self.add_option("Pause", "Resume", lambda: self.exit_menu())
        self.add_option("Pause", "Options", lambda: self.set_menu('Options'))
        self.add_option("Pause", "Credits", lambda: self.set_menu('Credits'))
        self.add_option("Pause", "Developer", lambda: self.set_menu('Developer'))
        self.add_option("Pause", "End", lambda: self.kill_game())

        self.add_menu('Options', 'Pause')
        self.add_option("Options", "Sound", lambda: self.set_menu("Sound"))
        self.add_option("Options", "Appearance", lambda: self.set_menu("Appearance"))
        self.add_option("Options", "Menu Color", lambda: self.set_menu("Choose Color"))

        self.add_menu('Sound', 'Options')
        self.add_option("Sound", "Enable audio", lambda: self.enable_audio())
        self.add_option("Sound", "Music volume", lambda: self.set_audio(self.classes['soundHelper'].music_channel))
        self.add_option("Sound", "Effects volume", lambda: self.set_audio(self.classes['soundHelper'].sfx_channel))

        self.add_menu('Appearance', 'Options')
        self.add_option("Appearance", "Since we use now a texture...", lambda: self.ui.say("Okay the texture looks better.."))
        self.add_option("Appearance", "Dark Theme", lambda: self.dark_theme())
        self.add_option("Appearance", "Light Theme", lambda: self.light_theme())

        self.add_menu('Choose Color', 'Options')
        for color in self.colors:
            self.add_option("Choose Color", str(color), lambda farbe: self.set_menu_color(self.primaryColor, farbe), color)

        self.add_menu('Credits', 'Pause')
        self.add_option("Credits", "A dog", lambda: self.ui.say('Wufff wuffff', True))
        self.add_option("Credits", "Git expert", lambda: self.ui.say('Schau mal mein Monitor!', True))
        self.add_option("Credits", "Graphic Designer", lambda: self.ui.say('Red line with transparent ink?', True))
        self.add_option("Credits", "ARISCH Drinking alpha", lambda: self.ui.say('Kocht auch sehr lecker und sorgt sich um das Teams', True))
        self.add_option("Credits", "Notepad++ Coder", lambda: self.ui.say('Muss mit Git expert in einem Zimmer schlafen uff', True))
        self.add_option("Credits", "Best coder of the world", lambda: self.ui.say("Codet die komplexe UI (beste am Spiel)", True))

        self.add_menu('Developer', 'Pause')
        self.add_option("Developer", "Dev play sounds", lambda: self.set_menu("Dev Play Sounds"))
        self.add_option("Developer", "DEBUG_DRAW_COLLISION", lambda: self.setTest())
        self.add_option("Developer", "DEV_CUT_SCENE", lambda: self.debug_cut_scene())
        self.add_option("Developer", "INTRO_SCENE", lambda: self.create_cut_scene_intro())
        self.add_option("Developer", "FIRST_ITEM", lambda: self.create_cut_scene_firstitem())
        self.add_option("Developer", "FIRST_KEY_CARD", lambda: self.create_cut_scene_firstkeycard())
        self.add_option("Developer", "THIRD_KEY_CARD", lambda: self.create_cut_scene_thirdkeycard())
        self.add_option("Developer", "OUTRO", lambda: self.create_cut_scene_outro())

        self.add_menu('Dev Play Sounds', 'Developer')
        self.add_option("Dev Play Sounds", "Play Dog Sound", lambda: classes['soundHelper'].play_sfx(classes['assets']['sounds']['bark'], 0))
        #print(self.menu)

        self.ui.say('ESC to pause game')

    def debug_cut_scene(self):
        self.ui.cut_scene.createCutScene([
            ['Message 1', {'color': (255, 0, 0)}],
            ['Message 2', {'color': (255, 255, 255)}],
            ['Message 3', {}],
        ])
    
    def create_cut_scene_intro(self):
        self.ui.cut_scene.createCutScene([
            ['Ahhhh… my head hurts.', {}],
            ['Bitchass bastards took away my beloved badge. ', {}],
            ['Suckers didn’t stop at my special sunglasses...', {}],
            ['The ones from Sander’s Supermarket Sunday Sale.', {}],
            ['But they missed the car keys in my butt crack hehehehe.', {}],
            ['But first I need to get out of here!', {}]
        ])

    def create_cut_scene_firstitem(self):
        self.ui.cut_scene.createCutScene([
            ['Man I wish this was a thomy mayonnaise.', {}],
            ['Day would be saved.', {}],
            ['But this one might come in handy as well.', {}]
        ])
        
    def create_cut_scene_firstkeycard(self):
        self.ui.cut_scene.createCutScene([
            ['These corrupt cops left key cards laying around.', {}],
            ['Luckily I ain’t no white girl, this card’s dirty as hell.', {}],
            ['Guess the dog played with this one.', {}],
            ['Can’t remember his name tho...', {}],
            ['...think it was something with Y…', {}]
        ])
        
    def create_cut_scene_thirdkeycard(self):
        self.ui.cut_scene.createCutScene([
            ['This trip was easier than handling git!', {}],
            ['Who built this prison? A bunch of drunk students?!', {}],
            ['Now I need to find the exit without being raped by aliens...', {}],
            ['...although...heh', {}]
        ])
    
    def create_cut_scene_outro(self):
        self.ui.cut_scene.createCutScene([
            ['Off I go, first stop - grandpa Nuknuk’s bar!', {}],
            ['Cool Cop is back on the road again!', {}]
        ])

    def enable_audio(self):
        if self.classes['soundHelper'].music_channel.get_volume() > 0 or self.classes['soundHelper'].sfx_channel.get_volume() > 0:
            self.classes['soundHelper'].music_channel.set_volume(0.0)
            self.classes['soundHelper'].sfx_channel.set_volume(0.0)
            self.ui.say('Audio disabled', True)
        else: 
            self.classes['soundHelper'].music_channel.set_volume(DEFAULT_MUSIC_VOLUME)
            self.classes['soundHelper'].sfx_channel.set_volume(DEFAULT_AUDIO_VOLUME)
            self.ui.say('Audio enabled', True)

    def set_audio(self, which):
        current_level = which.get_volume()
        if current_level >= 1:
            current_level = 0
        else:
            current_level += 0.1
        which.set_volume(current_level)
        self.ui.say('Set to ' + str(which.get_volume()), True)

    def kill_game(self):
        pygame.quit()

    def setTest(self):
        DEBUG_DRAW_COLLISION = True
        #print("DEBUG_DRAW_COLLISION: ", DEBUG_DRAW_COLLISION)

    def light_theme(self):
        self.primaryColor = self.colors[9]
        self.background = self.colors[2]

    def dark_theme(self):
        self.primaryColor = self.colors[2]
        self.background = self.colors[9]

    def set_menu_color(self, var, color):
        self.primaryColor = color

    def add_menu(self, name, parent = None, custom_display_name = None):
        if custom_display_name is None:
            custom_display_name = name

        self.menu[name] = {
            'options': [],
            'scroller': 0,
            'parent': parent,
            'name': custom_display_name
        }

    def add_option(self, menu_name, option_name, callback, parameter_one = None):
        if menu_name not in self.menu:
            # print(menu_name, " doesn't exist")
            return
        self.menu[menu_name]['options'].append({
            'name': option_name,
            'callback': callback,
            'parameter_one': parameter_one
        })
    
    def set_menu(self, menu_name, current_option = None):
        if menu_name not in self.menu:
            self.ui.say(menu_name, " doesn't exist")
            return

        if current_option is None:
            current_option = self.menu[menu_name]['scroller']

        if current_option > len(self.menu[menu_name]['options']) - 1:
            current_option = 0
            self.ui.say("The selected option is not there. Seems like something isn't working here. To bad!")
        self.current_menu = menu_name
        
        self.current_option = current_option

    def update(self):
        if self.open:
            self.ui.notification.x = 380
        else:
            self.ui.notification.x = 20

        if self.time_when_control is not None and pygame.time.get_ticks() > self.time_when_control:
            self.is_waiting = False
        if self.is_controlling is False and self.is_waiting is False:
            if self.open is not True and pygame.key.get_pressed()[pygame.K_ESCAPE]:
                self.is_waiting = True
                self.time_when_control = pygame.time.get_ticks() + self.time_wait_open
                self.open = True
                self.ui.say('ARROW KEYS to navigate', False, 300)
                self.ui.say('ENTER to select an option', False, 300)
                self.ui.say('ESC to go back/close', False, 300)
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
                    if self.menu[self.current_menu]['options'][self.current_option]['parameter_one'] is not None:
                        self.menu[self.current_menu]['options'][self.current_option]['callback'](self.menu[self.current_menu]['options'][self.current_option]['parameter_one'])
                    else:
                        self.menu[self.current_menu]['options'][self.current_option]['callback']()
                    self.time_when_control = pygame.time.get_ticks() + self.time_wait_use
                elif self.menu[self.current_menu]['parent'] == None and pygame.key.get_pressed()[pygame.K_ESCAPE] == True:
                    self.exit_menu()
                elif pygame.key.get_pressed()[pygame.K_ESCAPE] == True:
                    self.time_when_control = pygame.time.get_ticks() + self.time_wait_back
                    if self.menu[self.current_menu]['parent'] is not None:
                        self.set_menu(self.menu[self.current_menu]['parent'])

                #print("Current option is: ", self.current_option, " ", pygame.time.get_ticks())
                self.is_controlling = False
    
    def exit_menu(self):
        self.is_waiting = True
        self.time_when_control = pygame.time.get_ticks() + self.time_wait_open
        self.open = False

    def render(self, render):
        if self.open is False:
            return

        self.ui.uiHelper.createRectangle({
            'x': 0,
            'y': 0,
            'width': WINDOW_WIDHT / 3,
            'height': WINDOW_HEIGHT,
            'color': self.background,
            'render': render
        })

        self.ui.uiHelper.createSprite({
            'x': 0,
            'y': 0,
            'width': WINDOW_WIDHT,
            'height': WINDOW_HEIGHT,
            'texture' : self.classes['assets']['textures']['ui']['menu_background'],
            'render' : render
        })

        start_menu_options_x = WINDOW_WIDHT/30


        self.ui.uiHelper.createText(self.menu[self.current_menu]['name'], {
            'font': self.ui.uiHelper.fonts['headline']['font'],
            'render': render,
            'x': start_menu_options_x,
            'y': 100 - self.ui.uiHelper.fonts['headline']['font_height'],
            'color': self.primaryColor
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
                currentColor = self.primaryColor
            elif self.menu[self.current_menu]['name'] == 'Choose Color':
                currentColor = self.colors[index]
            else:
                currentColor = self.secondaryColor

            self.ui.uiHelper.createText(option['name'], {
                'font': self.ui.uiHelper.fonts['h2']['font'],
                'render': render,
                'x': start_menu_options_x,
                'y': 150 + self.ui.uiHelper.fonts['h2']['font_height'] * index,
                'color': currentColor
            })


            index += 1