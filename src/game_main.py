import pygame
import input_helper

window_dimensions = (800,800)

def launch_game():
    pygame.init()
    screen = pygame.display.set_mode(window_dimensions)
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

