
import pygame.font

class Button:
    """ A class for on-screen action buttons. """

    def __init__(self, game, label):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.width, self.height = 200, 50
        self.color = (0, 135, 0)
        self.label_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._init_label(label)

    def _init_label(self, label):
        self.label_image = self.font.render(label, True, self.label_color, self.color)
        self.label_rect = self.label_image.get_rect()
        self.label_rect.center = self.screen_rect.center

    def draw(self):
        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.label_image, self.label_rect)

        

