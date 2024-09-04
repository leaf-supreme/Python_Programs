# CCP_CH12_Practice_Problems
# 12.1 make a blue sky 
# i made mine following pygame documentation and it worked but not similar to book
# book used settings class and similar to AlienInvasion


import pygame 

class BlueScreen:
    """Create a class for blue screen settings"""
    
    def __init__(self):
        """Inilize the screen settings"""
        pygame.init()
        self.screen = pygame.display.set_mode((900, 700))
        self.clock = pygame.time.Clock()
        self.game_running = True
        
    def running(self):
        """Run time events for Blue screen"""
        while self.game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False
                    
            self.screen.fill((104,31,249))
            pygame.display.flip()
            self.clock.tick(30)
        pygame.quit()
        
if __name__ == '__main__':
    # Make a game instance and run a game
    bs = BlueScreen()
    bs.running()