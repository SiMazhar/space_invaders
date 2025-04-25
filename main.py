import pygame, sys

class Game:
    def __init__(self):
        pass

    def run(self):
        pass

if __name__ == "__main__":
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))  # Fill the screen with black
        pygame.display.flip()  # Update the display
        clock.tick(60)  # Limit to 60 frames per second