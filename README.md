# Space Invaders

A Python-based version of Space Invaders built with [pygame](https://www.pygame.org/).

## Overview

This repository implements a classic space shooter game featuring multiple components:
- **Player**: Controlled by the user, moves using arrow keys and shoots lasers with the spacebar.
- **Aliens**: Enemy sprites that move and periodically fire lasers.
- **Asteroids**: Random obstacles that fall from the top of the screen.
- **Boss**: A challenging enemy appearing at higher levels with its own shooting mechanics.

## Repository Structure

- **main.py**: Entry point for the game.
- **player.py**: Contains the [`Player`](c:\Users\kikiq\space_invaders\player.py) class.
- **asteroids.py**: Contains the [`Asteroid`](c:\Users\kikiq\space_invaders\asteroids.py) class.
- **aliens.py**: Contains the [`Aliens`](c:\Users\kikiq\space_invaders\aliens.py) class.
- **boss.py**: Contains the [`Boss`](c:\Users\kikiq\space_invaders\boss.py) class.
- **laser.py**: Contains the laser implementations used by the player.
- **graphics/**: Directory with image assets (e.g., player, alien, asteroid, and boss images).
- **test/**: Contains tests using pytest.
- **pytest.ini**: Configuration file for pytest.

## Requirements

- Python 3.x
- pygame

## Setup & Run

1. **Install Dependencies:**
   ```sh
   pip install pygame

2. **run**
   python main.py
