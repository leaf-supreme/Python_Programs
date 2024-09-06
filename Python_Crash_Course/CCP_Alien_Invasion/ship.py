# Class for ship in Alien Invasion 
import pygame
from settings import Settings

class Ship:
    """Class for ship in alien invasions"""
    
    def __init__(self, ai_game):
        """Intialize Ship class"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        
        # load the ship bmp from image folder
        self.image = pygame.image.load('images/shipp.bmp')
        self.rect = self.image.get_rect()
        
        # start a new ship at bottom mid of screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Store a float for ships exact hotizontal position 
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        # movement flag; start with a ship that isnt moving
        self.moving_right = False
        self.moving_left = False
        self.moving_foreward = False
        self.moving_backward = False
        
    def update(self):
        """Update ship position based on movement flag"""
        #update ships position x value not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_foreward:
            self.y -= self.settings.ship_speed
        if self.moving_backward:
            self.y += self.settings.ship_speed
            
        # Update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y
            
            
    def blitme(self):
        """Draw shop at its current location"""
        self.screen.blit(self.image, self.rect)
        
