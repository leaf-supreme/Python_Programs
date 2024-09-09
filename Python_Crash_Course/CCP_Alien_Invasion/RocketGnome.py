# CCP_CH12_Practice_Problems
# 12.1 make a blue sky tured into 12.4 Rocket(with a gnome)
# i made mine following pygame documentation and it worked but not similar to book
# book used settings class and similar to AlienInvasion


import pygame 
from rsettings import RSettings
from gnome import Gnome

class RocketGnome:
    """Create a class for blue screen settings"""
    
    def __init__(self):
        """Inilize the screen settings"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.rsettings = RSettings()
        self.rscreen = pygame.display.set_mode(
            (self.rsettings.rscreen_width,self.rsettings.rscreen_height))
        pygame.display.set_caption("H's Rocket Gnome")
        self.gnome = Gnome(self)
        self.game_running = True
        
    def running(self):
        """Run time events for Rocket Gnome"""
        while self.game_running:
            self._check_events()
            self.gnome.update()
            self._update_screen()
            self.clock.tick(69)
            
    def _check_events(self):
        """Checking events for Keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_running = False
            elif event.type == pygame.KEYDOWN:
                self._key_down_events(event)
            elif event.type == pygame.KEYUP:
                self._key_up_events(event)
                    
    def _key_down_events(self, event):
        """Helper flag for key_down events"""
        if event.key == pygame.K_RIGHT:
            self.gnome.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.gnome.moving_left = True
        elif event.key == pygame.K_UP:
            self.gnome.moving_foreward = True
        elif event.key == pygame.K_DOWN:
            self.gnome.moving_backward = True
        elif event.key == pygame.K_q:
            self.game_running = False
                    
    def _key_up_events(self, event):
        """Helper function for Key_up events"""
        if event.key == pygame.K_RIGHT:
            self.gnome.moving_right = False 
        elif event.key == pygame.K_LEFT:
            self.gnome.moving_left = False
        elif event.key == pygame.K_UP:
            self.gnome.moving_foreward = False
        elif event.key == pygame.K_DOWN:
            self.gnome.moving_backward = False
    
    def _update_screen(self):
        """Updates screen with a set refresh rate"""    
        self.rscreen.fill((self.rsettings.bkgrnd_color))
        self.gnome.bltime()
        pygame.display.flip()
    
if __name__ == '__main__':
    # Make a game instance and run a game
    rg = RocketGnome()
    rg.running()