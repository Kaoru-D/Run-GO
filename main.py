import pygame
import random
import sys 
from py import background_game, character_game, obstacles_game, autoscroll_game, points_game 


#Iniciatlize pygame
pygame.init()
#background's size
WIDTH = 800 
HIGH = 400
screen_game =  background_game.create_screen_game(WIDTH, HIGH)

# Color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
#Text
BASE_FONTS=pygame.font.get_fonts()[0]
BASE_FONT = pygame.font.SysFont(BASE_FONTS, 30)
#points
POINTS=0
score_text = BASE_FONT.render("Points: 0", True, BLACK) # I need to initiallize the text just in case the user don't avoid th first obstacle
# Player size and propeties
player, speed_y, jump_count = character_game.create_character(HIGH)
MAX_JUMPS=2 
obstacles_game.create_obstacles(WIDTH, HIGH)

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
                character_game.jump_character()
        if evento.type == new_obstacle:            
            obstacle = pygame.Rect(WIDTH, HIGH - 70, 40, 40)# this method take the coordenates for the obstacle
            obstacles_game.create_obstacles.append(obstacle)# obstacles it's a array, so just add a new item to the array
            

    # Movement player (gravity)
    speed_y += 1
    character_game.user_character.y += speed_y # it's a acumulator on the y axis
    if character_game.user_character.y >= HIGH - 70:# this conditional see if the user it's on the air
        character_game.user_character.y = HIGH - 70
        speed_y=0
        jump_count=0 #reset the value when touch the floor

    # Here draw the player like the same canvas.create_rectangle()
    pygame.draw.rect(screen_game, BLACK, character_game.user_character)

    # The obstacles are the ones that moved not the player
    for obstacle in list(obstacles_game.obstacles):
        obstacle.x -= 5 #here get close to the player
        pygame.draw.rect(screen_game, RED, obstacle) #the obstacle it's red
        if obstacle.colliderect(character_game.user_character):# here take the collition of the obstacle and the player
            print("Game Over!!... ")
            pygame.quit()
            sys.exit()
        if obstacle.x < -50:# if the player doesn't collide the obstacle keep moving 
            # Render the text
            POINTS, score_text = points_game.points(POINTS, BLACK, BASE_FONT) # this function render the points and update the text
            obstacles_game.obstacles.remove(obstacle) # when the obstacle are on -51 in the x axis remove the item on the array
            
        screen_game.blit(score_text, (WIDTH - 100, 10))#this function print the text
    
    pygame.display.flip()#this function reset all the values or update the screen

pygame.quit()