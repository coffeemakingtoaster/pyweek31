from collections import defaultdict

class Hud():

    def __init__(self, ui, classes):
        self.ui = ui
        self.classes = classes
        self.primaryColor = (255,255,255)
        self.countColor = (0,0,0)
        self.player_inventory = defaultdict(lambda:0)


    def update(self):
        pass


    def render(self, render):

        if self.ui.menu.open or self.ui.cut_scene.is_active:
            return

        self.ui.uiHelper.createSprite({
            'x': 206,
            'y': 395,
            'width': 50,
            'height': 50,
            'texture' : self.classes['assets']['textures']['items']['coffee'],
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

        self.ui.uiHelper.createSprite({
            'x': 293,
            'y': 395,
            'width': 50,
            'height': 50,
            'texture' : self.classes['assets']['textures']['items']['coin'],
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

        self.ui.uiHelper.createSprite({
            'x': 379,
            'y': 395,
            'width': 50,
            'height': 50,
            'texture' : self.classes['assets']['textures']['items']['donut'],
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

        self.ui.uiHelper.createSprite({
            'x': 466,
            'y': 395,
            'width': 50,
            'height': 50,
            'texture' : self.classes['assets']['textures']['items']['jammer'],
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
        