import pygame

class Ship:
    """ Class for the player's ship. """

    def __init__(self, game):
        """ Initialize the ship. """
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

    # Origin of 'blit': https://en.wikipedia.org/wiki/Bit_blit.
    def blitme(self):
        """ Draw the ship. """
        self.screen.blit(self.image, self.rect)


