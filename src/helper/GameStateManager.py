
# load
# play
# pause
# cutscene
# quit

class GameStateManager(): 
    def __init__(self):
        self.game_state = "load"

    def set_game_state(self, game_state):
        self.game_state = game_state

    def is_play(self):
        return self.game_state == "play"

    def is_cutscene(self):
        return self.game_state == "cutscene"