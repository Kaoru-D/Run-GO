import pygame

def points_game(total,color,font):
    total+=1
    
    points_text = font.render(f"Points: {total}", True, color)
    return total, points_text