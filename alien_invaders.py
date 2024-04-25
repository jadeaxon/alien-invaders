# Alien Invaders game from the Python Crash Course book.

import os
import sys
from time import sleep
import pygame

script_dir = os.path.dirname(__file__)
# Make location of this file our working directory. Else relative paths will be screwed up.
os.chdir(script_dir)

# I've also added this directory to PYTHONPATH in Windows.

from settings import Settings
from ship import Ship
# Why does this give a warning while the ship module is found fine?
from bullet import Bullet # type: ignore
from alien import Alien # type: ignore
from game_stats import GameStats # type: ignore
from button import Button # type: ignore
from scoreboard import Scoreboard # type: ignore

class AlienInvaders:
    """ Class to represent the overall game. """

    def __init__(self):
        """ Initialize the game. """
        pygame.init()
        # To keep a consistent frame rate, pygame will pause before showing next video frame if there is extra time.
        # Otherwise, the faster your computer, the faster the game would run. You could see this in old DOS games.
        self.settings = Settings()
        self.stats = GameStats(self)
        self.clock = pygame.time.Clock()

        if self.settings.fullscreen:
            # Fullscreen mode.
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        else:
            self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption(self.settings.caption)
        self.ship = Ship(self) # The ship knows it is part of this game.
        self.scoreboard = Scoreboard(self)
        self.bullets = pygame.sprite.Group() # Like a list.
        self.bullet_count = 0
        self.aliens = pygame.sprite.Group()
        self.alien_count = 0
        self.game_active = False # Is a game in progress?
        self.play_button = Button(self, "Play")

        # Do this when play button pressed.
        # self._create_alien_fleet()

    def _create_alien_fleet(self):
        alien = Alien(self)
        self.aliens.add(alien)
        w = alien.rect.width
        h = alien.rect.height
        x = w
        y = h
        
        # Create multiple rows of aliens.
        while y < (self.settings.screen_height - (3 * h)):
            # Create a row of aliens.
            while x < (self.settings.screen_width - (2 * w)):
                self._create_alien(x, y)            
                x += 2 * w
            x = w
            y += 2 * h

    def _create_alien(self, x, y):
        alien = Alien(self)
        self.aliens.add(alien)
        alien.x = x
        alien.rect.x = x
        alien.y = y
        alien.rect.y = y


    def run_game(self):
        """ Start the main game loop. """
        # self.game_active = True
        print("Running Alien Invasion.")
        while True:
            # Check for player input.
            self._check_events()

            if self.game_active:
                # Update the game world.
                self._update_game_world()
                
            # Render the new state of the game world.
            self._update_screen()

            # Advance time in the game world.
            self.clock.tick(60) # Tick at 60 frames per second.

    # Helper methods (private instance methods).
    # Start with _ by convention.
    def _check_events(self):
        ship = self.ship
        # Get list of events that have happened since we last checked for events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = True
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet()
                elif event.key == pygame.K_q:
                    sys.exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    ship.moving_left = False

    def _check_play_button(self, mouse_pos):
        # The play button DNE when the game is active.
        if self.game_active: return

        if self.play_button.rect.collidepoint(mouse_pos):
            self.game_active = True
            self.settings.reset()
            self.stats.reset()
            self.scoreboard.reset()
            self.bullets.empty()
            self.aliens.empty()
            self._create_alien_fleet()

    def _update_game_world(self):
        self.ship.update()
        self.bullets.update()

        # Get rid of off-screen bullets. Otherwise you have a memory leak.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        bullet_count = len(self.bullets)
        if bullet_count != self.bullet_count:
            print('bullets: ' + str(bullet_count))
            self.bullet_count = bullet_count

        # Check for bullet collisions with aliens.
        # The final two args cause both the bullets and aliens to be deleted.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values(): 
                self.stats.score += len(aliens) * self.settings.alien_points
            self.scoreboard.update()

        # If the fleet gets destroyed, create a new fleet. Speed up the game.
        if not self.aliens:
            self.bullets.empty()
            self._create_alien_fleet()
            self.settings.speed_up()

        # Check for alien/ship collision.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("Ship hit!")
            self._ship_hit()

        self._check_fleet_edges()
        self._check_aliens_bottom() # Have aliens reach the bottom of the screen?
        self.aliens.update()
        self.scoreboard.update()

    def _check_aliens_bottom(self):
        """ Check if aliens have reached the bottom of the screen. """
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit() # Treat this condition as if ship got hit.
                break

    def _ship_hit(self):
        """ Handles when ship gets hit (or alien reaches bottom of screen)."""
        self.stats.ships_left -= 1
        self.bullets.empty()
        self.aliens.empty()
        if self.stats.ships_left == 0:
            print("GAME OVER: The alien invasion was successful.")
            self.game_active = False
            return
        self._create_alien_fleet()
        self.ship.center()
        sleep(0.5)

    def _update_screen(self):
        if not self.game_active:
            self.play_button.draw()
        else:
            # pygame.display.update() # Is this needed?
            self.screen.fill(self.settings.bg_color)
            self.ship.draw()
            for bullet in self.bullets.sprites():
                bullet.draw()
            # for alien in self.aliens.sprites():
                # alien.draw()
            self.aliens.draw(self.screen)
            self.scoreboard.draw()
        
        pygame.display.flip() # Show the updated the display.

    def _fire_bullet(self):
        bullet = Bullet(self)
        # Only allow a fixed number of bullets to be fired at once.
        if len(self.bullets) < self.settings.bullet_limit:
            self.bullets.add(bullet)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """ Drop the fleet vertically and change horizontal movement direction. """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1 # Reverse direction.

# Runs this if called as a script.
if __name__ == '__main__':
    # Make the game instance and run it.
    print("Running __main__.")
    game = AlienInvaders()
    game.run_game()
