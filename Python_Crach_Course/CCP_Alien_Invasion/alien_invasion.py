# First program starting the Crash_Course_Practice for the Alien Invasion Prject

import sys
import pygame 

class AlienInvasion():
    """Overall Class to manage fame assets and behavior"""
    
    def __init__(self):
        """Initilize Game, and create game resources"""
        pygame.init()
        
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("H's Alien Invasion")
        
    def run_game(self):
        """Start main loop for the game"""
        while True:
            # watch for keybard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            # Make the most recentle drawn screen visible.
            pygame.display.flip()
if __name__ == '__main__':
    # Make a game instance and run a game
    ai = AlienInvasion()
    ai.run_game()