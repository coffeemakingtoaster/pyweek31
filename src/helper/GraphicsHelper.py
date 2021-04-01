import pygame
from .. import config

class frame_handler():
    def __init__(self,x_dimension,y_dimension):
        frame_size = (x_dimension,y_dimension)
        self.frame = pygame.Surface(frame_size)

    def refresh_frame():
        generate_hud()
        
    def draw_background():
        pass

    def draw_hud():
        test_rect = pygame.Rect(0,0,x_dimension/3,y_dimension/3)
        pygame.draw.rect(self.frame,(255,255,255),test_rect)
        
class render_helper():
    def rotate_image(image, angle):
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image
    
    def convert_to_screen_cords(player,x,y):
        x = x - player.x  + config.WINDOW_WIDHT/2
        y = y - player.y + config.WINDOW_HEIGHT/2
        return (x,y)