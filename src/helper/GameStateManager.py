
# load
# play
# pause
# cutscene
# quit
# reset
# victory
# over

class GameStateManager(): 
    def __init__(self):
        self.game_state = "load"

    def set_game_state(self, game_state):
        print(self.game_state, " is getting updated to ", game_state)            
        self.game_state = game_state


    def is_play(self):
        return self.game_state == "play"

    def is_cutscene(self):
        return self.game_state == "cutscene"
    
    def is_reset(self):
        return self.game_state == "reset"
    
    def is_victory(self):
        return self.game_state == "victory"
    
    def is_over(self):
        return self.game_state == "over"
    
    def is_checkpointReached(self):
        return self.game_state == "checkpoint"

    def is_kriha(self):
        return self.game_state == "kriha"