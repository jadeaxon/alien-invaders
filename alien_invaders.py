# Alien Invaders game from the Python Crash Course book.

import sys
import pygame # type: ignore

class AlienInvasion:
    """ Class to represent the overall game. """

    def __init__(self):
        """ Initialize the game. """
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """ Start the main game loop. """
        print("Running Alien Invasion.")
        while True:
            # Get list of events that have happened since we last checked for events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.display.update()
            pygame.display.flip() # Show the updated the display.

# Runs this if called as a script.
if __name__ == '__main__':
    # Make the game instance and run it.
    print("Running __main__.")
    game = AlienInvasion()
    game.run_game()
