import pygame
import random
import sys 
import os #necessary for the path of the images
from py import background_game, character_game, obstacles_game


#Iniciatlize pygame
pygame.init()
#background's size
WIDTH = 800 
HEIGHT = 400
screen_game =  background_game.create_screen_game(WIDTH, HEIGHT)

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
player_img= character_game.MySprite(WIDTH/8,HEIGHT-100)  # take the position of the player
player_sprite = pygame.sprite.Group()  # this method create a group of sprites, in this case the player
player_sprite.add(player_img)  # add the player to the group of sprites

# Physics
gravity = 0.8  # Gravity constant  
speed_y = 0 # this variable is for the gravity
jump_count = 0 # this variable is for the jumps
MAX_JUMPS=2 
is_jumping = False  # Flag to check if the character is jumping
GROUND_LEVEL = HEIGHT - 100  # Ground level height

# Obstacles
obstacles = []
obstacle_timer = pygame.time.get_ticks()
OBSTACLE_FREQUENCY = 1500  # 1.5 seconds

# Clock
clock_time = pygame.time.Clock() # this method works the same way that a normal clock ascend every second

# Main Loop
runnig = True
while runnig:
    # Run the game
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:# here it's the conditional to go out to the loop
            runnig = False
        if evento.type == pygame.KEYDOWN:# analyse if the user it's pressing the button
            if evento.key == pygame.K_SPACE and jump_count < MAX_JUMPS:# here just counts if it's the bar space execute the function
                speed_y = -15  # Jump's force              jump_count += 1
                is_jumping = True
                player_img.on_ground = False  # Mark that the player is not on the ground
    
    # Aply gravity
    if not player_img.on_ground:  # Will be true if the player is not on the ground
        speed_y += gravity
        player_img.rect.y += speed_y
    
    # Verify if the player is jumping    
    if player_img.rect.bottom >= GROUND_LEVEL:
        # Adjust the player's position to the ground level
        player_img.rect.bottom = GROUND_LEVEL
        speed_y = 0  # Reset vertical speed when landing
        jump_count = 0
        is_jumping = False
        player_img.on_ground = True  # Mark that the player is on the ground
    else:
        player_img.on_ground = False  # Mark that the player is not on the ground
              
    # Obstacle generation 
    current_time = pygame.time.get_ticks()  # Get the current time in milliseconds             
    if current_time - obstacle_timer > OBSTACLE_FREQUENCY:
        obstacle_timer = current_time
        obstacle_height = random.randint(30, 70)
        obstacle = pygame.Rect(WIDTH, HEIGHT-100 - obstacle_height , 40, obstacle_height)
        obstacles.append(obstacle)
        
    # Move and draw obstacles
    screen_game.fill(WHITE)
    for obstacle in obstacles[:]:
        obstacle.x -= 5  # Velocity of the obstacle moving towards the player
        player_rect = player_img.rect
        
        # Check for collision with the player
        if player_rect.colliderect(obstacle):
            print("¡Colisión! Game Over")
            running = False
        
        # Eliminate obstacles that go off-screen
        if obstacle.right < 0:
            obstacles.remove(obstacle)
            POINTS += 1  # Add points for avoiding the obstacle
            if BASE_FONT:
                score_text = BASE_FONT.render(f"Points: {POINTS}", True, BLACK)
        
        # Draw the obstacle
        pygame.draw.rect(screen_game, RED, obstacle)
        
    player_sprite.update()  # Update the player sprite 
    player_sprite.draw(screen_game)  # Draw the player sprite on the screen        
    
    
    # Here draw the player like the same canvas.create_rectangle()
    #pygame.draw.rect(screen_game, BLACK, player)
    
    # Draw the score text
    if score_text:
        screen_game.blit(score_text, (10, 10))
    # Draw the ground
    pygame.draw.rect(screen_game, (100, 100, 100), (0, GROUND_LEVEL, WIDTH, HEIGHT - GROUND_LEVEL))  # Draw the ground rectangle
    
    pygame.display.flip()#this function reset all the values or update the screen
    clock_time.tick(60)  # Limit the frame rate to 60 FPS

pygame.quit()
# Movement player (gravity)
# Pre-cargar imágenes

