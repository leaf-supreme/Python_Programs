# Class for ship in Alien Invasion 
import pygame

class Ship():
    """Class for ship in alien invasions"""
    
    def __init__(self, ai_game):
        """Intialize Ship class"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        # load the ship bmp from image folder
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        
        # start a new ship at bottom mid of screen
        self.rect.midbottom = self.screen_rect.midbottom
        
    def blitme(self):
        """Draw shop at its current location"""
        self.screen.blitme(self.image, self.rect)
        