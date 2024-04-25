import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ Class to represent a single alien invader. """

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height  
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """ Return true if alien at edge of screen. """
        s = self.screen.get_rect()
        return (self.rect.right >= s.right) or (self.rect.left <= 0)
    



