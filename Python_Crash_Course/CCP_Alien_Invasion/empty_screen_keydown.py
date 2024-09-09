# CCP Trying to run 12.4 with nothing but keydown events to see what happends

import pygame

def empty_screen():
    """Creating an empty scren that will test keydown events"""
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800,500),pygame.display.set_caption("emptyniess"))
    game_running = True
    
def keydown(event):
    while game_running == True:
        if event.key == pygame.KEYDOWN:
            print(event.key)
        elif event.key == pygame.K_q:
            game_running = False
            pygame.quit()
            
def update_screen():
    screen.fill((250,250,250))
    pygame.display.flip()
       