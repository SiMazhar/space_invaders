import pygame
import sys
import random
from asteroids import Asteroid

ASTEROID_SPAWN_EVENT = pygame.USEREVENT + 1

class Game:
    def __init__(self):
        
        self.asteroids = pygame.sprite.Group()
        
    def run(self):
        self.asteroids.update()
        self.asteroids.draw(screen)

 

if __name__ == "__main__":
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = Game()

    # schedule ASTEROID_SPAWN_EVENT every 200 ms
    pygame.time.set_timer(ASTEROID_SPAWN_EVENT, 200)
    # remember when we started spawning
    spawn_start = pygame.time.get_ticks()
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == ASTEROID_SPAWN_EVENT:
                elapsed = pygame.time.get_ticks() - spawn_start
                if elapsed <= 15_000:
                    # still within 10 seconds → spawn one
                    game.asteroids.add(Asteroid())
                else:
                    # >10 seconds → stop the timer
                    pygame.time.set_timer(ASTEROID_SPAWN_EVENT, 0)


        screen.fill((0, 0, 0))  # Fill the screen with black
        game.run()
        pygame.display.flip()  # Update the display
        clock.tick(60)  # Limit the frame rate to 60 FPS

   