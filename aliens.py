import pygame

class AlienLaser(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((3, 15))
        self.image.fill((0, 255, 0))  # green laser
        self.rect = self.image.get_rect(midtop=pos)
        self.speed = 5

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > pygame.display.get_surface().get_height():
            self.kill()

class Aliens(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        file_path = "graphics\green.png"
        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 2            # new movement speed
        self.direction = 1        # 1: moving right, -1: moving left
        self.lasers = pygame.sprite.Group()  # group for alien lasers
        self.last_shot = pygame.time.get_ticks()  # time of last shot
        self.shoot_delay = 2000   # shoot every 2 seconds

    def update(self):
        screen = pygame.display.get_surface()
        sw = screen.get_width()
        if self.direction == 1 and self.rect.right >= sw:
            self.rect.y += 20
            self.direction = -1
        elif self.direction == -1 and self.rect.left <= 0:
            self.rect.y += 20
            self.direction = 1
        else:
            self.rect.x += self.speed * self.direction
        
        self.lasers.update()  # update lasers
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot > self.shoot_delay:  # shoot every 2 seconds
            self.shoot()
            self.last_shot = current_time

    def shoot(self):
        # Shoot a green laser downward from the alien's bottom center.
        self.lasers.add(AlienLaser((self.rect.centerx, self.rect.bottom)))