#Class for my gnome character
import pygame 
from rsettings import RSettings

class Gnome:
    """Setting up class for gnome character"""

    def __init__(self, gnome):
        """Initilizing Gnome Character Class"""
        self.rscreen = gnome.rscreen
        self.rscreen_rect = gnome.rscreen.get_rect()
        self.rsettings = gnome.rsettings
        
        # load image sprite
        self.image = pygame.image.load("Python_Crash_Course/CCP_Alien_Invasion/images/gnomer.bmp")
        self.rect = self.image.get_rect()
        
        # start at mid center of screen
        self.rect.center = self.rscreen_rect.center
        
        # store positions as a float value
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        # movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_foreward = False
        self.moving_backward = False
        
    def update(self):
        """Update ships position based on movement flag"""
        if self.moving_right and self.rect.right < self.rscreen_rect.right:
                self.x += self.rsettings.gnome_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.rsettings.gnome_speed
        if self.moving_foreward and self.rect.top > 0:
            self.y -= self.rsettings.gnome_speed
        if self.moving_backward and self.rect.bottom < self.rscreen_rect.bottom:
            self.y += self.rsettings.gnome_speed
        # update rect obj from self.x and .y
        self.rect.x = self.x
        self.rect.y = self.y
            
    def  bltime(self):
        """Copy Gnome sruface onto screen surface"""
        self.rscreen.blit(self.image, self.rect)