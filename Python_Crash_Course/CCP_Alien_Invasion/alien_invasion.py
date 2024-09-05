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
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)   #set framerate to 60 sec based upon computer clock
    
    def _check_events(self):
        """Respond to keypress and mouse event"""
         # watch for keybard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_UP:
                    self.ship.moving_foreward = True
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_backward = True
                    
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False 
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                elif event.key == pygame.K_UP:
                    self.ship.moving_foreward = False
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_backward = False
    
    def _update_screen(self):
        """Updates image on scren and flip to new screen"""
        # redraw the screen during each pass through the loop
        self.screen.fill(self.settings.bkgnd_color)
        self.ship.blitme()    # i had this after pygame.display and ship didnt show up
        # Make the most recentle drawn screen visible.
        pygame.display.flip()
            
if __name__ == '__main__':
    # Make a game instance and run a game
    ai = AlienInvasion()
    ai.run_game()