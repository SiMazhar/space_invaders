import pygame
import random
from time import sleep


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, a):
        super().__init__()
        self.image = pygame.image.load("graphics/asteroid.png").convert_alpha()
        place = [(random.randint(0, 800), random.randint(-400, -40)), (random.randint(-400, -40), random.randint(50, 600)), (random.randint(840, 1240), random.randint(50, 600)), (random.randint(1240, 1940), random.randint(50, 600)), (random.randint(0, 800), random.randint(-800, -400)), (random.randint(-800, -400), random.randint(50, 600))]
        self.rect = self.image.get_rect(midtop=place[a])
        self.velocity = 2
        if a == 0:
            self.direction = random.randint(-5, 5)
        elif a == 1:
            self.direction = random.randint(0, 5)
        elif a == 2:
            self.direction = random.randint(-5, 0)
        elif a == 3:
            self.direction = -1
            self.velocity = 1
        elif a == 4:
            self.direction = random.randint(-1, 1)
        elif a == 5:
            self.direction = 1
            self.velocity = 1
    
    def destroy(self):
        if self.rect.y >= 650:
           self.kill()

    def update(self):
        self.rect.y += self.velocity
        self.rect.x += self.direction
        self.destroy()