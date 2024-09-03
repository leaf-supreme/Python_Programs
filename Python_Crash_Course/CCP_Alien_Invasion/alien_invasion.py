# First program starting the Crash_Course_Practice for the Alien Invasion Prject

import sys
import pygame 
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall Class to manage fame assets and behavior"""
    
    def __init__(self):
        """Initilize Game, and create game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("H's Alien Invasion")
        self.clock = pygame.time.Clock() 
        self.ship = Ship(self)
        
    def run_game(self):
        """Start main loop for the game"""
        while True:
            # watch for keybard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            # redraw the screen during each pass through the loop
            self.screen.fill(self.settings.bkgnd_color)
            self.ship.blitme()    # i had this after pygame.display and ship didnt show up
                    
            # Make the most recentle drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)   #set framerate to 60 sec based upon computer clock
            
if __name__ == '__main__':
    # Make a game instance and run a game
    ai = AlienInvasion()
    ai.run_game()