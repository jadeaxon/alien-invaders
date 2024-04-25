class Settings:
    """ A class to store all the settings for the Alien Invasion game. """

    def __init__(self):
        """ Initialize the game's settings. """
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230) # Light gray.
        self.caption = "Alien Invaders"
        self.fullscreen = False

        # Ship settings.
        self.ship_speed = 3.5

        # Bullet settings.
        self.bullet_speed = 2.0
        self.bullet_width = 6
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_limit = 10 # Number of bullets allowed at once.

        # Alien settings.
        self.alien_speed = 1.0
        self.fleet_direction = 1 # 1 is right; -1 left.
        self.fleet_drop_speed = 10




