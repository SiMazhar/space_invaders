import pygame, sys
from player import Player
from aliens import Aliens

class Game:
    def __init__(self):
        player_sprite = Player((screen_width / 2, screen_height), screen_width, screen_height, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        self.aliens = pygame.sprite.Group()
        self.alien_setup()

    def alien_setup(self):
        for row in range(1):
            for column in range(1):
                x = column * 100 + 50
                y = row * 50 + 50
                alien = Aliens(x, y)
                self.aliens.add(alien)
        

    def run(self):
        self.player.update()
        self.aliens.update()  # update aliens using their move function
        # Check collision: remove player laser and alien on hit
        pygame.sprite.groupcollide(self.player.sprite.lasers, self.aliens, True, True)
        self.aliens.draw(screen)
        # Draw lasers from all aliens
        for alien in self.aliens:
            alien.lasers.draw(screen)
        self.player.sprite.lasers.draw(screen)  # Draw the player laser
        self.player.draw(screen)

if __name__ == "__main__":
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))  # Fill the screen with black
        game.run()
        pygame.display.flip()  # Update the display
        clock.tick(60)  # Limit to 60 frames per second