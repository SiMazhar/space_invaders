import pygame
import random

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, level, screen_width, screen_height):
        super().__init__()
        self.image = pygame.image.load("graphics/asteroid.png").convert_alpha()
        self.rect = self.image.get_rect()
        # Spawn at a random border.
        spawn_side = random.choice(['top', 'bottom', 'left', 'right'])
        if spawn_side == 'top':
            self.rect.x = random.randint(0, screen_width - self.rect.width)
            self.rect.y = -self.rect.height
        elif spawn_side == 'bottom':
            self.rect.x = random.randint(0, screen_width - self.rect.width)
            self.rect.y = screen_height
        elif spawn_side == 'left':
            self.rect.x = -self.rect.width
            self.rect.y = random.randint(0, screen_height - self.rect.height)
        else:  # right
            self.rect.x = screen_width
            self.rect.y = random.randint(0, screen_height - self.rect.height)

            
        velocity = pygame.math.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        if velocity.length() == 0:
            velocity = pygame.math.Vector2(1, 0)
        if level == 4:
            self.velocity = velocity.normalize() * 2  # fixed speed at level 4
        elif level == 8:
            self.velocity = velocity.normalize() * 5  # fixed speed at level 8
        else:
            self.velocity = pygame.math.Vector2(0, 0)  # no velocity at other levels

    def update(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
        screen = pygame.display.get_surface()
        if (self.rect.right < 0 or self.rect.left > screen.get_width() or
            self.rect.bottom < 0 or self.rect.top > screen.get_height()):
            self.kill()
