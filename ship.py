import pygame
from settings import Settings

class Ship:
    """ Class for the player's ship. """

    def __init__(self, game):
        """ Initialize the ship. """
        self.settings = Settings()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        # The top left of the game screen is (0, 0).
        self.image = pygame.image.load('images/ship.bmp')
        # Each game element is treated as a rectangle for collision purposes.
        self.rect = self.image.get_rect()

        # Put ship at middle of bottom of screen.
        # How does this work? It does calculations behind the scenes so they align even though different widths.
        # The variable is probably really a property with associated getter/setter methods.
        self.rect.midbottom = self.screen_rect.midbottom

        # User holding down a key is like having a maneuvering thruster engaged.
        self.moving_right = False
        self.moving_left = False

    # Origin of 'blit': https://en.wikipedia.org/wiki/Bit_blit.
    def blitme(self):
        """ Draw the ship. """
        self.screen.blit(self.image, self.rect)

    def draw(self):
        self.blitme()

    def update(self):
        if self.moving_right:
            self.move_right()
        if self.moving_left:
            self.move_left()

    def move_right(self):
        """ Moves the ship to the right. """
        if self.rect.right < self.screen_rect.right:
            self.rect.x += int(self.settings.ship_speed)

    def move_left(self):
        """ Moves the ship to the left. """
        if self.rect.left > 0:
            self.rect.x -= int(self.settings.ship_speed)

            

    



