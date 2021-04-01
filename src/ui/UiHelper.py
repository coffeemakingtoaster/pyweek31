import pygame
import os

from .. import config

class UiHelper:

    def __init__(self):
        self.fonts = {
            'text': {
                'font': self.createFont({
                    'font_size': 24,
                    'font_type': os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'font', 'dogicapixel.ttf'),
                }),
                'font_height': 30
            },
            'h2': {
                'font': self.createFont({
                    'font_size': 30,
                    'font_type': os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'font', 'dogicapixel.ttf'),
                }),
                'font_height': 64
            },
            'headline': {
                'font': self.createFont({
                    'font_size': 56,
                    'font_type': os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'font', 'dogicapixel.ttf'),
                }),
                'font_height': 88
            },
        }

    def createFont(self, props):
        font = pygame.font.Font(props['font_type'], props['font_size'])
        return font 

    def createText(self, text, props):
        font = props['font'].render(text, True, props['color'])
        props['render'].frame.blit(font, (props['x'], props['y']))

    def createRectangle(self, props):
        pygame.draw.rect(props['render'].frame, props['color'], pygame.Rect(props['x'], props['y'], props['width'], props['height'])) 
    
    def createSprite(self, props):
        props['texture'] = pygame.transform.scale(props['texture'], (config.TILE_SIZE, config.TILE_SIZE))  
        props['render'].frame.blit(props['texture'], (props['x'], props['y']))