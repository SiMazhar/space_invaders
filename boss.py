import pygame

class BossLaser(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((3, 15))
        self.image.fill((255, 0, 0))  # green laser
        self.rect = self.image.get_rect(midtop=pos)
        self.speed = 5

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > pygame.display.get_surface().get_height():
            self.kill()

class Boss(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        file_path = "graphics\\red.png"
        self.image = pygame.image.load(file_path).convert_alpha()
        # Scale the boss image 5x bigger.
        original_size = self.image.get_size()
        new_size = (original_size[0] * 5, original_size[1] * 5)
        self.image = pygame.transform.scale(self.image, new_size)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 2            # new movement speed
        self.direction = 1        # 1: moving right, -1: moving left
        self.lasers = pygame.sprite.Group()  # group for boss lasers
        self.last_shot = pygame.time.get_ticks()  # time of last shot
        self.shoot_delay = 4000   # shoot delay in ms
        self.health = 30         # new: boss needs 30 hits to die

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
        # Shoot 3 lasers at once, arranged in a row with 20 pixels spacing.
        base_x = self.rect.centerx
        base_y = self.rect.bottom
        for offset in [-40, 0, 40]:
            self.lasers.add(BossLaser((base_x + offset, base_y)))