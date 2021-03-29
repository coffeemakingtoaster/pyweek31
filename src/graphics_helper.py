import pygame

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