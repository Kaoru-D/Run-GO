import pygame
import random
import sys 
import os #necessary for the path of the images
from py import background_game, character_game, obstacles_game, autoscroll_game, points_game 


#Iniciatlize pygame
pygame.init()
#background's size
WIDTH = 800 
HEIGHT = 400
screen_game, screen_size =  background_game.create_screen_game(WIDTH, HEIGHT)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Text
BASE_FONTS=pygame.font.get_fonts()[0]
BASE_FONT = pygame.font.SysFont(BASE_FONTS[0] if BASE_FONTS else None, 30)  # Use the first available font or a default one

# Points
POINTS=0
score_text = BASE_FONT.render("Points: 0", True, BLACK) # I need to initiallize the text just in case the user don't avoid th first obstacle

# Player size and propeties
player_img= character_game.MySprite(WIDTH/8,HEIGHT)  # take the position of the player
player_sprite = pygame.sprite.Group()  # this method create a group of sprites, in this case the player
player_sprite.add(player_img)  # add the player to the group of sprites


speed_y = 0 # this variable is for the gravity
jump_count = 0 # this variable is for the jumps
MAX_JUMPS=2 
obstacles = obstacles_game.create_obstacles(WIDTH, HEIGHT)


clock_time = pygame.time.Clock() # this method works the same way that a normal clock ascend every second
new_obstacle = pygame.USEREVENT + 1
pygame.time.set_timer(new_obstacle, 1500)  # each 1.5s




# Main Loop
runnig = True
while runnig:
    print("Running")
    clock_time.tick(60)
    screen_game.fill(WHITE)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:# here it's the conditional to go out to the loop
            runnig = False
        if evento.type == pygame.KEYDOWN:# analyse if the user it's pressing the button
            if evento.key == pygame.K_SPACE:# here just counts if it's the bar space execute the function
                character_game.jump_character(MAX_JUMPS)
        if evento.type == new_obstacle:            
            obstacle = pygame.Rect(WIDTH, HEIGHT - 70, 40, 40)# this method take the coordenates for the obstacle
            obstacles.append(obstacle)# obstacles it's a array, so just add a new item to the array
    player_sprite.update()  # Update the player sprite (if using sprite groups)
    
    player_sprite.draw(screen_game)  # Draw the player sprite on the screen        

    


    # Here draw the player like the same canvas.create_rectangle()
    #pygame.draw.rect(screen_game, BLACK, player)
    screen_game.blit(player, (screen_size[0]-screen_size[0],
                              screen_size[1]-screen_size[1])) # this method draw the player on the screen
    # The obstacles are the ones that moved not the player
    """ for obstacle in list(obstacles):
        obstacle.x -= 5 #here get close to the player
        pygame.draw.rect(screen_game, RED, obstacle) #the obstacle it's red
        if obstacle.colliderect(player):# here take the collition of the obstacle and the player
            print("Game Over!!... ")
            pygame.quit()
            sys.exit()
        if obstacle.x < -50:# if the player doesn't collide the obstacle keep moving 
            # Render the text
            POINTS, score_text = points_game.points(POINTS, BLACK, BASE_FONT) # this function render the points and update the text
            obstacles.remove(obstacle) # when the obstacle are on -51 in the x axis remove the item on the array
                """
    screen_game.blit(score_text, (WIDTH - 100, 10))#this function print the text
    
    pygame.display.flip()#this function reset all the values or update the screen

pygame.quit()
# Movement player (gravity)
def jump_character(max_jumps):
    global speed_y, jump_count #convert the properties of the user global for use on all the program
    if jump_count < max_jumps: #this conditional check if the user is on air
        speed_y = -15 
        jump_count += 1