import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ Class to represent a single alien invader. """

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height  
        self.x = float(self.rect.x)


