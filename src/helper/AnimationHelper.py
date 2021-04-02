from .. import config


class AnimatedGameObject():
    def __init__(self, x, y, assets, game_state):
        self.x = 0
        self.y = 0
        self.ticks_passed = 0
        self.assets = assets
        self.game_state = game_state
    
    def get_current_asset(self, needs_update):
        if needs_update and self.game_state.is_play():
             self.ticks_passed +=1
        if self.ticks_passed < config.FRAME_TIME:          
            return self.assets[0]
        elif self.ticks_passed == config.FRAME_TIME*2:
            self.ticks_passed = 0          
        return self.assets[1]
            
        
            