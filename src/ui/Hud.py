class Hud():

    def __init__(self, ui, classes):
        self.ui = ui
        self.classes = classes


    def update(self):
        pass


    def render(self, render):
        self.ui.uiHelper.createSprite({
            'x': 206,
            'y': 395,
            'width': 50,
            'height': 50,
            'texture' : self.classes['assets']['textures']['items']['coffee'],
            'render': render
        })

        self.ui.uiHelper.createSprite({
            'x': 293,
            'y': 395,
            'width': 50,
            'height': 50,
            'texture' : self.classes['assets']['textures']['items']['coin'],
            'render': render
        })

        self.ui.uiHelper.createSprite({
            'x': 379,
            'y': 395,
            'width': 50,
            'height': 50,
            'texture' : self.classes['assets']['textures']['items']['donut'],
            'render': render
        })

        self.ui.uiHelper.createSprite({
            'x': 466,
            'y': 395,
            'width': 50,
            'height': 50,
            'texture' : self.classes['assets']['textures']['items']['jammer'],
            'render': render
        })