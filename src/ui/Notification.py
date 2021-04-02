from ..config import *

class Notification():

    def __init__(self, ui):
        self.uiHelper = ui.uiHelper
        self.notifications = []
        self.x = 20
        self.y = WINDOW_HEIGHT - 40
        self.is_active = False

    def pushNotification(self, text, props):
        if props['force_display'] == False:
            for notification in self.notifications:
                if notification['message'] == text:
                    return

        self.notifications[:0] = [{
            'message': text,
            'time': props['time'],
            'color': props['color']
        }]
        

    def render(self, render):
        if self.is_active is not True:
            return
            
        index = 0
        for notification in self.notifications:
            if notification['time'] > 0:
                notification['time'] -= 1
            else:
                notification['time'] = 0
                self.notifications.remove(notification)
                continue

            self.uiHelper.createText(notification['message'], {
                'font': self.uiHelper.fonts['text']['font'],
                'render': render,
                'x': self.x,
                'y': self.y - self.uiHelper.fonts['text']['font_height'] * index,
                'color': notification['color']
            })
            index += 1



