from pygame import mixer
from random import randrange

class SoundHelper():
    def __init__(self):
        self.music_channel = mixer.Channel(0)
        self.music_channel.set_volume(0.3)
        self.sfx_channel = mixer.Channel(1)
        self.sfx_channel.set_volume(0.3)
        self.cache = []

        #Can be set to false for example in settings menu
        self.allowSFX = True

    """Use this to play sfx sounds
    Args:
        sfx: Name of the sound in the assets[sounds]
        loopsCount: The number of loops to be played, -1 for infinite
    """
    def play_sfx(self, sfx, loopsCount):
        if self.allowSFX and not self.sfx_channel.get_busy():
            if isinstance(sfx, list): 
                if len(self.cache) == 0:
                    self.cache = sfx[:]
        
                currentSoundKey = 0 if len(self.cache) <= 1 else randrange(len(self.cache))

                self.sfx_channel.play(self.cache[currentSoundKey], loopsCount)
                del self.cache[currentSoundKey]
            else:
                self.sfx_channel.play(sfx, loopsCount)
  
    """Use this to play music
    Args:
        music: Name of the music in the assets[sounds]
        loopsCount: The number of loops to be played, -1 for infinite
    """
    def play_music(self, music, loopsCount):
        if not self.music_channel.get_busy():
            self.music_channel.play(music, loopsCount)