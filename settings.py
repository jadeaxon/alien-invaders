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
        self.initial_ship_speed = 3.5
        self.ship_speed = self.initial_ship_speed
        self.ships_at_start = 3

        # Bullet settings.
        self.initial_bullet_speed = 5.0
        self.bullet_speed = self.initial_bullet_speed
        self.bullet_width = 6
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_limit = 10 # Number of bullets allowed at once.

        # Alien settings.
        self.initial_alien_speed = 2.0
        self.alien_speed = self.initial_alien_speed
        self.fleet_direction = 1 # 1 is right; -1 left.
        self.initial_fleet_drop_speed = 20
        self.fleet_drop_speed = self.initial_fleet_drop_speed
        self.alien_points = 50

        self.speedup_factor = 1.1

    def reset(self):
        self.ship_speed = self.initial_ship_speed
        self.bullet_speed = self.initial_bullet_speed
        self.alien_speed = self.initial_alien_speed
        self.fleet_drop_speed = self.initial_fleet_drop_speed

    def speed_up(self):
        self.fleet_drop_speed *= self.speedup_factor
        self.bullet_speed *= self.speedup_factor
        self.ship_speed *= self.speedup_factor
        self.alien_speed *= self.speedup_factor




