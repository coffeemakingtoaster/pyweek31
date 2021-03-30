from pygame import mixer

class SoundHelper():
    def __init__(self):
        self.music_channel = mixer.Channel(0)
        self.music_channel.set_volume(0.3)
        self.sfx_channel = mixer.Channel(1)
        self.sfx_channel.set_volume(0.3)

        #Can be set to false in settings menu
        self.allowSFX = True

    def play_sfx(self, sfx):
        if allowSFX:
            self.sfx_channel.play(sfx)

    def play_music(self, music, loops):
        self.music_channel.play(music, loops)
