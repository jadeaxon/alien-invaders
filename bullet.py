import pygame
from pygame.sprite import Sprite
from random import randint

class Bullet(Sprite):
    """ Class for bullets fired from the ship. """

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = self.game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        # Make the bullet move upward at its speed.
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

