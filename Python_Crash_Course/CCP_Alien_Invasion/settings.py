# Setting for Alien invasions game

class Settings:
    """Settings for Alien Invasions"""
    
    def __init__(self):
        """Initlize Game Settings"""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bkgnd_color = (45,53,94)   #background RGB
        # Ship settings 
        self.ship_speed = 20.5 #1.5 pixels but rect uses only integers 
        # Bullet settings
        self.bullet_speed = 12.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0,255,0)
        