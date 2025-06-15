import pygame
import os

class MySprite(pygame.sprite.Sprite):
    def __init__(self, images):
        super().__init__()
        self.images = images
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = 50  # Initial x position
        self.rect.y = 300  # Initial y position
        
    def create_character():
    # Player size and propeties
        route = os.path.join(os.path.dirname(__file__),"..", "img","player")  # Get the directory of the current file
        user_character = [pygame.image.load(f"{route}/RunAttack1.png").convert_alpha(),
                      pygame.image.load(f"{route}/RunAttack2.png").convert_alpha(),
                      pygame.image.load(f"{route}/RunAttack3.png").convert_alpha(),
                      pygame.image.load(f"{route}/RunAttack4.png").convert_alpha(),
                      pygame.image.load(f"{route}/RunAttack5.png").convert_alpha(),
                      pygame.image.load(f"{route}/RunAttack6.png").convert_alpha()]# Load the character images
        return [pygame.transform.scale(image, (50, 50)) for image in user_character]  # Scale the images to 50x50 pixels

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 100:  # change image every 100 ms
            self.last_update = now
            self.current_frame = (self.current_frame + self.animation_speed) % len(self.animation_frames)
            self.image = self.animation_frames[int(self.current_frame)]