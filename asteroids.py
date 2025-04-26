import pygame
import random


class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("graphics/asteroid.png").convert_alpha()
        place = [(random.randint(0, 800), -40), (-40, random.randint(50, 600)), (840, random.randint(50, 600))]
        a = random.randint(0, 2)
        self.rect = self.image.get_rect(midtop=place[a])
        self.velocity = 2
        if a == 0:
            self.direction = random.randint(-5, 5)
        elif a == 1:
            self.direction = random.randint(0, 5)
        else:
            self.direction = random.randint(-5, 0)
    
    def destroy(self):
        if self.rect.y >= 650:
           self.kill()

    def update(self):
        self.rect.y += self.velocity
        self.rect.x += self.direction
        self.destroy()