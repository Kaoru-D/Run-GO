import pygame
from typing import Tuple

def create_screen_game(width,high):
    pygame.init()
    screen_size: Tuple[int, int] = (width, high)
    screen_game = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Runner: Jump the Obstacle")
    
    return screen_game