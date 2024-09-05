# Class for ship in Alien Invasion 
import pygame

class Ship:
    """Class for ship in alien invasions"""
    
    def __init__(self, ai_game):
        """Intialize Ship class"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # load the ship bmp from image folder
        self.image = pygame.image.load('images/shipp.bmp')
        self.rect = self.image.get_rect()
        
        # start a new ship at bottom mid of screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        # movement flag; start with a ship that isnt moving
        self.moving_right = False
        self.moving_left = False
        self.moving_foreward = False
        self.moving_backward = False
        
    def update(self):
        """Update ship position based on movement flag"""
        if self.moving_right:
            self.rect.x +=1
        if self.moving_left:
            self.rect.x -=1
        if self.moving_foreward:
            self.rect.y -=1
        if self.moving_backward:
            self.rect.y +=1
            
    def blitme(self):
        """Draw shop at its current location"""
        self.screen.blit(self.image, self.rect)
        
