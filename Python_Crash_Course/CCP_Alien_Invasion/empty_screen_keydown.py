# CCP Trying to run 12.4 with nothing but keydown events to see what happends

import pygame

pygame.init()
#pygame.display.set_caption("emptyniess")

screen = pygame.display.set_mode([800,500])

game_running = True
while game_running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            print(pygame.KEYDOWN)
            print(event.key)
            
    
    screen.fill((250,250,250))    
    
    pygame.display.flip()

#Below is the books version but it to does not actually display kepress on screen just in terminal
#we esentially created similar games but in wildly different ways 
'''import sys

from settings import Settings


class KeyGame:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Key Game")

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        # Show the key that was pressed, then quit if q was pressed.
        #   For more information about the output, see here:
        #   https://www.pygame.org/docs/ref/key.html
        print(event.key)
        if event.key == pygame.K_q:
            sys.exit()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bkgnd_color)
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    kg = KeyGame()
    kg.run_game()'''
    
