# Alien Invaders game from the Python Crash Course book.

import os
import sys
import pygame

script_dir = os.path.dirname(__file__)
# Make location of this file our working directory. Else relative paths will be screwed up.
os.chdir(script_dir)

# I've also added this directory to PYTHONPATH in Windows.

from settings import Settings
from ship import Ship

class AlienInvasion:
    """ Class to represent the overall game. """

    def __init__(self):
        """ Initialize the game. """
        pygame.init()
        # To keep a consistent frame rate, pygame will pause before showing next video frame if there is extra time.
        # Otherwise, the faster your computer, the faster the game would run. You could see this in old DOS games.
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.caption)
        self.ship = Ship(self) # The ship knows it is part of this game.

    def run_game(self):
        """ Start the main game loop. """
        print("Running Alien Invasion.")
        while True:
            # Get list of events that have happened since we last checked for events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # pygame.display.update() # Is this needed?
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            pygame.display.flip() # Show the updated the display.
            self.clock.tick(60) # Tick at 60 frames per second.

# Runs this if called as a script.
if __name__ == '__main__':
    # Make the game instance and run it.
    print("Running __main__.")
    game = AlienInvasion()
    game.run_game()
