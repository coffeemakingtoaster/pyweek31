from ..config import *

class Notification():

    def __init__(self, ui):
        self.uiHelper = ui.uiHelper
        self.notifications = []
        self.fontHeight = 20
        self.x = 20
        self.y = WINDOW_HEIGHT - 40

    def pushNotification(self, text, props):
        for notification in self.notifications:
            if notification['message'] == text:
                return
        print(text, " is printed to the screen as notification!")

        self.notifications[:0] = [{
            'message': text,
            'time': props['time'],
            'color': props['color']
        }]
        

    def render(self, render):
        index = 0
        for notification in self.notifications:
            if notification['time'] > 0:
                notification['time'] -= 1
            else:
                notification['time'] = 0
                self.notifications.remove(notification)
                continue
            
            self.uiHelper.createText(notification['message'], {
                'font': self.uiHelper.fonts['text'],
                'render': render,
                'x': self.x,
                'y': self.y - self.fontHeight * index,
                'color': notification['color']
            })
            index += 1



