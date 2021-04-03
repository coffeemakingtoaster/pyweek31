from .. import config

from random import randint
class AnimatedGameObject():
    def __init__(self, x, y, assets, game_state, frame_time = None):
        if frame_time is None:
            self.frame_time = config.FRAME_TIME
        else: 
            self.frame_time = frame_time
        self.x = 0
        self.y = 0
        self.ticks_passed = randint(0,(self.frame_time*2)-1)
        self.assets = assets
        self.game_state = game_state
    
    def get_current_asset(self, needs_update):
        if needs_update and (self.game_state.is_play() or self.game_state.is_cutscene()):
             self.ticks_passed +=1
        if self.ticks_passed < self.frame_time:          
            return self.assets[0]
        elif self.ticks_passed == self.frame_time*2:
            self.ticks_passed = 0          
        return self.assets[1]
            
        
            