import pygame

class Aliens(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        file_path = "graphics\green.png"
        self.image = pygame.image.load(file_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 2            # new movement speed
        self.direction = 1        # 1: moving right, -1: moving left

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