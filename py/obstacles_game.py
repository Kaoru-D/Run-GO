import pygame
import os

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, obstacle_type, ground_level):
        super().__init__()
        
        # Load obstacle images
        self.images = self.load_obstacle_images()
        
        # Select obstacle type
        self.type = obstacle_type
        self.image = self.images[self.type]
        self.rect = self.image.get_rect()
        
        # Initialize position
        self.rect.x = 800  # Comienza fuera de la pantalla a la derecha
        self.rect.bottom = ground_level
        
        # Movement speed
        self.speed = 5
        
        # Configure damage based on obstacle type
        if self.type == 0:  # obstacle type 1
            self.damage = 10
        else:  # obstacle type 2
            self.damage = 20
    
    def load_obstacle_images(self):
        """Carga y escala las imágenes de obstáculos"""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        img_dir = os.path.join(current_dir, "..", "img", "obstacles")
        
        images = []
        try:
            # Load first type of obstacle
            img1 = pygame.image.load(os.path.join(img_dir, "rock.png")).convert_alpha()
            img1 = pygame.transform.scale(img1, (60, 60))  # Scale to a different size
            images.append(img1)
            
            # Load second type of obstacle
            img2 = pygame.image.load(os.path.join(img_dir, "tree.png")).convert_alpha()
            img2 = pygame.transform.scale(img2, (80, 40))  # Scale to a different size
            images.append(img2)
        except Exception as e:
            print(f"Error cargando imágenes de obstáculos: {e}")
            # Create placeholder images if loading fails
            placeholder1 = pygame.Surface((60, 60), pygame.SRCALPHA)
            placeholder1.fill((255, 0, 0, 128))  # Red transparent
            images.append(placeholder1)
            
            placeholder2 = pygame.Surface((80, 40), pygame.SRCALPHA)
            placeholder2.fill((0, 0, 255, 128))  # Blue transparent
            images.append(placeholder2)
        
        return images
    
    def update(self):
        """Move the obstacle to the left"""
        self.rect.x -= self.speed
        
        # Delete the obstacle if it goes off-screen
        if self.rect.right < 0:
            self.kill()