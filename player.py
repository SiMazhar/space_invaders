import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, constraints_x, constraints_y, speed):
        super().__init__()
        self.image = pygame.image.load("graphics\player.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = pos)
        self.speed = speed
        self.max_x_constraints = constraints_x
        self.max_y_constraints = constraints_y



    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        
    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_x_constraints:
            self.rect.right = self.max_x_constraints
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.max_y_constraints:
            self.rect.bottom = self.max_y_constraints


    def update(self):
        self.get_input()
        self.constraint()  # ensure player remains within screen bounds
