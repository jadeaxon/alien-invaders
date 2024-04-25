import pygame.font

class Scoreboard:
    """ A class to display game score. """

    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats
        
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self._update_score()
        
    def _update_score(self):
        # Render and position score.
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def reset(self):
        self.score = 0
        self._update_score()

    def update(self):
        self._update_score()

    def draw(self):
        self.screen.blit(self.score_image, self.score_rect)

    
