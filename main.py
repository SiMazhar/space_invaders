import pygame, sys
from player import Player

class Game:
    def __init__(self):
        player_sprite = Player((screen_width / 2, screen_height))
        self.player = pygame.sprite.GroupSingle(player_sprite)

    def run(self):
        self.player.draw(screen)
        self.player.update()

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