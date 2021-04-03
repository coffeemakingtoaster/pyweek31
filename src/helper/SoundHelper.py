from pygame import mixer
from random import randrange
import random

from ..config import *


class SoundHelper():
    def __init__(self):
        self.music_channel = mixer.Channel(0)
        self.music_channel.set_volume(DEFAULT_MUSIC_VOLUME)
        self.sfx_channel = mixer.Channel(1)
        self.sfx_channel.set_volume(DEFAULT_AUDIO_VOLUME)
        self.sfx2_channel = mixer.Channel(2)
        self.sfx2_channel.set_volume(DEFAULT_AUDIO_VOLUME)
        self.atmo_channel = mixer.Channel(3)
        self.atmo_channel.set_volume(DEFAULT_AUDIO_VOLUME)
        self.cache = []
        self.gamestate_channel = mixer.Channel(4)
        self.gamestate_channel.set_volume(DEFAULT_AUDIO_VOLUME)

        #Can be set to false for example in settings menu
        self.allowSFX = True
        self.allowMusic = True

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
    
    def play_atmo_sound(self, sfx):
        #this is the coolest random sound player ever hehehehehehe
         if self.allowSFX and not self.atmo_channel.get_busy() and random.randint(0,100)==69:
                self.atmo_channel.play(random.choice(sfx), 1)

         
    def play_tickless_sfx(self, sfx, loopsCount):
        if self.allowSFX and not self.sfx2_channel.get_busy():
            if isinstance(sfx, list): 
                self.sfx2_channel.play(random.choice(sfx), loopsCount)
            else:
                self.sfx_channel.play(sfx, loopsCount)
                
    def play_gamestate_sfx(self, sfx, loopsCount):
        if self.allowSFX and not self.gamestate_channel.get_busy():
            if isinstance(sfx, list): 
                self.gamestate_channel.play(random.choice(sfx), loopsCount)
            else:
                self.gamestate_channel.play(sfx, loopsCount)
  
    """Use this to play music
    Args:
        music: Name of the music in the assets[sounds]
        loopsCount: The number of loops to be played, -1 for infinite
    """
    def play_music(self, music, loopsCount):
        if not self.music_channel.get_busy() and self.allowMusic:
            self.music_channel.play(music, loopsCount)