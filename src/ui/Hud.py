from collections import defaultdict
from ..config import *

class Hud():

    def __init__(self, ui, classes):
        self.ui = ui
        self.classes = classes
        self.game_state = self.classes['game_state']
        self.primaryColor = (255,255,255)
        self.countColor = (0,0,0)
        self.player_inventory = defaultdict(lambda:0)
        self.player_keycards = []
        self.avaible_keycards = ["green","red","blue"]


    def update(self):
        pass


    def render(self, render):

        if self.ui.menu.open or self.ui.cut_scene.is_active:
            return

        card_index = 0
        for color in self.avaible_keycards:
            if color in self.player_keycards:
                card_visual = self.classes['assets']['textures']['keycards'][color]
            else:
                card_visual = self.classes['assets']['textures']['keycards']["grey"]
            self.ui.uiHelper.createSprite({
                'x': 650,
                'y': 71 + card_index * 55,
                'width': 44,
                'height': 44,
                'texture' : card_visual,
                'render': render
            })
            card_index+=1
            
        if self.player_inventory["coffee"] == 0:
            coffee_visual = self.classes['assets']['textures']['empty_items']['coffee']
        else:
           coffee_visual = self.classes['assets']['textures']['items']['coffee']
        self.ui.uiHelper.createSprite({
            'x': 206,
            'y': 395,
            'width': 50,
            'height': 50,
            'texture' : coffee_visual,
            'render': render
        })
        
        
        self.ui.uiHelper.createText("1", {
            'font': self.ui.uiHelper.fonts['text']['font'],
            'render': render,
            'x': 206,
            'y': 475 - self.ui.uiHelper.fonts['text']['font_height'],
            'color': self.primaryColor
        })
        
        self.ui.uiHelper.createText(str(self.player_inventory["coffee"]), {
            'font': self.ui.uiHelper.fonts['text']['font'],
            'render': render,
            'x': 206 + 40,
            'y': 460 - self.ui.uiHelper.fonts['h2']['font_height'],
            'color': self.countColor
        })

        if self.player_inventory["coin"] == 0:
            coin_visual = self.classes['assets']['textures']['empty_items']['coin']
        else:
           coin_visual = self.classes['assets']['textures']['items']['coin']
        self.ui.uiHelper.createSprite({
            'x': 293,
            'y': 395,
            'width': 50,
            'height': 50,
            'texture' : coin_visual,
            'render': render
        })
        
        self.ui.uiHelper.createText("2", {
            'font': self.ui.uiHelper.fonts['text']['font'],
            'render': render,
            'x': 293,
            'y': 475 - self.ui.uiHelper.fonts['text']['font_height'],
            'color': self.primaryColor
        })
        
        self.ui.uiHelper.createText(str(self.player_inventory["coin"]), {
            'font': self.ui.uiHelper.fonts['text']['font'],
            'render': render,
            'x': 293 + 40,
            'y': 460 - self.ui.uiHelper.fonts['h2']['font_height'],
            'color': self.countColor
        })

        if self.player_inventory["donut"] == 0:
            donut_visual = self.classes['assets']['textures']['empty_items']['donut']
        else:
           donut_visual = self.classes['assets']['textures']['items']['donut']
        
        self.ui.uiHelper.createSprite({
            'x': 379,
            'y': 395,
            'width': 50,
            'height': 50,
            'texture' : donut_visual,
            'render': render
        })
        
        self.ui.uiHelper.createText("3", {
            'font': self.ui.uiHelper.fonts['text']['font'],
            'render': render,
            'x': 379,
            'y': 475 - self.ui.uiHelper.fonts['text']['font_height'],
            'color': self.primaryColor
        })
        
        self.ui.uiHelper.createText(str(self.player_inventory["donut"]), {
            'font': self.ui.uiHelper.fonts['text']['font'],
            'render': render,
            'x': 379 + 40,
            'y': 460 - self.ui.uiHelper.fonts['h2']['font_height'],
            'color': self.countColor
        })

        if self.player_inventory["jammer"] == 0:
            jammer_visual = self.classes['assets']['textures']['empty_items']['jammer']
        else:
           jammer_visual = self.classes['assets']['textures']['items']['jammer']
        
        self.ui.uiHelper.createSprite({
            'x': 466,
            'y': 395,
            'width': 50,
            'height': 50,
            'texture' : jammer_visual,
            'render': render
        })
        
        self.ui.uiHelper.createText("4", {
            'font': self.ui.uiHelper.fonts['text']['font'],
            'render': render,
            'x': 466,
            'y': 475 - self.ui.uiHelper.fonts['text']['font_height'],
            'color': self.primaryColor
        })
        
        self.ui.uiHelper.createText(str(self.player_inventory["jammer"]), {
            'font': self.ui.uiHelper.fonts['text']['font'],
            'render': render,
            'x': 466 + 40,
            'y': 460 - self.ui.uiHelper.fonts['h2']['font_height'],
            'color': self.countColor
        })


        if self.game_state.is_over():
            self.ui.uiHelper.createSprite({
                'x': 0,
                'y': 0,
                'width': WINDOW_WIDHT,
                'height': WINDOW_HEIGHT,
                'texture' : self.classes['assets']['textures']['ui']['game_over'],
                'render': render
            })

            self.ui.uiHelper.createText("Press R to reset to last checkpoint", {
                'font': self.ui.uiHelper.fonts['text']['font'],
                'render': render,
                'x': WINDOW_WIDHT/2 - 200,
                'y': WINDOW_HEIGHT/2 + 100,
                'color': (255, 255, 255)
            })

        