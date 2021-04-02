import pygame
import os

from .. import config

class UiHelper:

    def __init__(self):
        self.fonts = {
            'text': {
                'font': self.createFont({
                    'font_size': 16,
                    'font_type': os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'font', 'dogicapixel.ttf'),
                }),
                'font_height': 24
            },
            'h2': {
                'font': self.createFont({
                    'font_size': 20,
                    'font_type': os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'font', 'dogicapixel.ttf'),
                }),
                'font_height': 28
            },
            'headline': {
                'font': self.createFont({
                    'font_size': 40,
                    'font_type': os.path.join(os.path.dirname( __file__ ), '..', '..', 'data', 'font', 'dogicapixel.ttf'),
                }),
                'font_height': 48
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
        if 'width' not in props:
            props['width'] = config.TILE_SIZE

        if 'height' not in props:
            props['height'] = config.TILE_SIZE
        props['texture'] = pygame.transform.scale(props['texture'], (props['width'] , props['height'] ))  
        props['render'].frame.blit(props['texture'], (props['x'], props['y']))


    ### Format Stuff
    
    def formatTime(self, time):
        timeArray = []

        #get seconds
        total_seconds = time / 1000

        #get minutes
        minutes = int(total_seconds // 60)
        if minutes < 10:
            minutes = str(0) + str(minutes)
        timeArray.append(minutes)

        #get rest seconds
        rest_seconds = round(total_seconds % 60, 2)
        if rest_seconds < 10:
            rest_seconds = str(0) + str(rest_seconds)

        timeArray.append(rest_seconds)
        

        return timeArray
