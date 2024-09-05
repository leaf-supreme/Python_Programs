#Class for my gnome character
import pygame 

class Gnome:
    """Setting up class for gnome character"""

    def __init__(self, gnome):
        """Initilizing Gnome Character Class"""
        self.bscreen = gnome.bscreen
        self.bscreen_rect = gnome.bscreen.get_rect()
        
        # load image sprite
        self.image = pygame.image.load("images/gnomer.bmp")
        self.rect = self.image.get_rect()
        
        # start at mid center of screen
        self.rect.center = self.bscreen_rect.center
        
    def  bltime(self):
        """Copy Gnome sruface onto screen surface"""
        self.bscreen.blit(self.image, self.rect)