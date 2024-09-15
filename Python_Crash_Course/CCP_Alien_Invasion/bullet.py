#Bullet Class
import pygame 
from pygame.sprite import Sprite 
from settings import Settings

class Bullet(Sprite):
    """Class to manage Bullets for Alien Invasion"""
    
    def __init__(self,ai_game):
        """Initlize the bullet class"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        # Create a bullet rect at (0,0) then set correct position
        self.rect = pygame.Rect(0,0, self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        # Store the bullets position as a float 
        self.y = float(self.rect.y)
        
    def update(self):
        """Move Bullet on screen"""
        #update exact pos of bullet
        self.y -= self.settings.bullet_speed
        #update rect position
        self.rect.y = self.y
        
    def draw_bullet(self):
        """Draw bullet on screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
        