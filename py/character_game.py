import pygame

def create_character(high):
    # Player size and propeties
    user_character = pygame.Rect(100, high - 70, 50, 50)#here create the size of the character
    speed_y = 0
    jump_count=0
    return user_character, speed_y, jump_count

def jump_character(max_jumps):
    global speed_y, jump_count #convert the properties of the user global for use on all the program
    if jump_count < max_jumps: #this conditional check if the user is on air
        speed_y = -15 
        jump_count += 1