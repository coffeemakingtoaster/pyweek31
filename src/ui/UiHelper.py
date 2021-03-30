import pygame

class UiHelper:

    def __init__(self):
        self.fonts = {
            'text': self.createFont({
                'font_size': 24
            })
        }

    def createFont(self, props):
        font = pygame.font.SysFont(None, props['font_size'])
        return font 

    def createText(self, text, props):
        font = props['font'].render(text, True, props['color'])
        props['render'].frame.blit(font, (props['x'], props['y']))

    def createRectangle(self, props):
        pygame.draw.rect(props['render'].frame, props['color'], pygame.Rect(props['x'], props['y'], props['width'], props['height'])) 