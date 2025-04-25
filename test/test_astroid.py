import pygame
import pytest
from asteroids import Asteroid

# Fixture to initialize a tiny headless Pygame display so Surfaces can be created.
@pytest.fixture(autouse=True)
def init_pygame():
    pygame.display.init()
    pygame.display.set_mode((1, 1))  # dummy 1×1 surface
    yield
    pygame.display.quit()

# Monkeypatch pygame.image.load to avoid file I/O.
@pytest.fixture
def dummy_image(monkeypatch):
    surf = pygame.Surface((16, 16), pygame.SRCALPHA)
    monkeypatch.setattr(pygame.image, 'load', lambda path: surf)
    return surf

def test_velocity_magnitude_level_4(dummy_image):
    ast = Asteroid(level=4, screen_width=800, screen_height=600)
    vx, vy = ast.velocity.x, ast.velocity.y
    speed = (vx*vx + vy*vy) ** 0.5
    assert pytest.approx(speed, rel=1e-6) == 2

def test_velocity_magnitude_level_8(dummy_image):
    ast = Asteroid(level=8, screen_width=800, screen_height=600)
    vx, vy = ast.velocity.x, ast.velocity.y
    speed = (vx*vx + vy*vy) ** 0.5
    assert pytest.approx(speed, rel=1e-6) == 5

def test_spawn_on_edge(dummy_image):
    W, H = 200, 100
    # force many samples to catch all edges
    seen = set()
    for _ in range(100):
        ast = Asteroid(level=4, screen_width=W, screen_height=H)
        x, y = ast.rect.x, ast.rect.y
        if y < 0:
            seen.add('top')
        elif y > H:
            seen.add('bottom')
        elif x < 0:
            seen.add('left')
        elif x > W:
            seen.add('right')
    assert seen == {'top', 'bottom', 'left', 'right'}
