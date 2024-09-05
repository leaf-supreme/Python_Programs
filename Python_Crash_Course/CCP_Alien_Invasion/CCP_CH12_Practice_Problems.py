# CCP_CH12_Practice_Problems
# 12.1 make a blue sky 
# i made mine following pygame documentation and it worked but not similar to book
# book used settings class and similar to AlienInvasion


import pygame 
from bsettings import BSettings
from gnome import Gnome

class BlueScreen:
    """Create a class for blue screen settings"""
    
    def __init__(self):
        """Inilize the screen settings"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.bsettings = BSettings()
        self.bscreen = pygame.display.set_mode(
            (self.bsettings.bscreen_height,self.bsettings.bscreen_width))
        pygame.display.set_caption("H's BlueScreen Goodness")
        self.gnome = Gnome(self)
        self.game_running = True
        
    def running(self):
        """Run time events for Blue screen"""
        while self.game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False
                    
            self.bscreen.fill((self.bsettings.bkgrnd_color))
            self.gnome.bltime()
            pygame.display.flip()
            self.clock.tick(69)
        pygame.quit()
        
if __name__ == '__main__':
    # Make a game instance and run a game
    bs = BlueScreen()
    bs.running()