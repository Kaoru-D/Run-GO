import pygame

def create_screen_game(width,high):
    pygame.init()
    screen_game = pygame.display.set_mode((width, high))
    pygame.display.set_caption("Runner: Jump the Obstacle")
    
    return screen_game