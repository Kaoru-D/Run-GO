import pygame

def create_obstacles(width, high):
    # Obstacles Functions determine when appear an obstacle
    obstacles = []
    new_obstacle = pygame.USEREVENT + 1
    pygame.time.set_timer(new_obstacle, 1500)  # each 1.5s

    return obstacles