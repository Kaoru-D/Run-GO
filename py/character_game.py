import pygame
import os

class MySprite(pygame.sprite.Sprite):
    _cached_images = None
    def __init__(self, x, y):  # Constructor with position parameters
        super().__init__()
        if MySprite._cached_images is None:
            MySprite._cached_images = self.load_character_images()
        self.animation_frames = MySprite._cached_images  # load character images
        self.current_frame = 0
        self.animation_speed = 0.2
        self.image = self.animation_frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)  # use the parameters to set the position of the player
        self.last_update = pygame.time.get_ticks()
        self.on_ground = False  # Attribute to check if the player is on the ground
    def load_character_images(self):
        """Load and scale character images."""
        # Obtain a liable path to the images directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        img_dir = os.path.join(current_dir, "..", "img", "player")
        
        # Load images and handle errors
        images = []
        for i in range(1, 7):
            try:
                img_path = os.path.join(img_dir, f"RunAttack{i}.png")
                img = pygame.image.load(img_path).convert_alpha()
                img = pygame.transform.scale(img, (50, 50))
                images.append(img)
            except pygame.error as e:
                print(f"Error cargando imagen: {img_path}")
                print(e)
                # Create a placeholder image if the image cannot be loaded
                placeholder = pygame.Surface((50, 50), pygame.SRCALPHA)
                placeholder.fill((255, 0, 255, 128))  # Transparent magenta
                images.append(placeholder)
        
        return images
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 100:  # change image every 100 ms
            self.last_update = now
            self.current_frame = (self.current_frame + self.animation_speed) % len(self.animation_frames)
            self.image = self.animation_frames[int(self.current_frame)]
            
