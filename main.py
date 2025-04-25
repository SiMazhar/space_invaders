import pygame, sys, random
from player import Player
from aliens import Aliens


class Game:
    def __init__(self):
        player_sprite = Player((screen_width / 2, screen_height), screen_width, screen_height, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        self.aliens = pygame.sprite.Group()
        self.level = 1  # Initialize the level
        self.alien_setup()


    def alien_setup(self):
        self.aliens.empty()  # clear existing aliens
        if self.level == 1:
            # Level 1: single alien formation
            for row in range(1):
                for column in range(1):
                    x = column * 100 + 50
                    y = row * 50 + 50
                    alien = Aliens(x, y)
                    self.aliens.add(alien)
        elif self.level in (2, 3):
            # For levels 2 and 3: number of aliens increases by 2 from previous level.
            # Level 2: 1+2*(2-1)=3 aliens; Level 3: 1+2*(3-1)=5 aliens.
            num_aliens = 1 + 2 * (self.level - 1)
            total_spacing = (num_aliens - 1) * 200  # spacing between aliens is 60 pixels
            start_x = (screen_width - total_spacing) // 2
            y = 50
            for i in range(num_aliens):
                x = start_x + i * 200
                alien = Aliens(x, y)
                self.aliens.add(alien)
        # ...existing code for other levels if any...


    def run(self):
        self.player.update()
        self.aliens.update()  # update aliens using their move function
        
        # Check if any alien laser hits player; if so, display "You Lose!" and exit.
        for alien in self.aliens:
            if pygame.sprite.spritecollide(self.player.sprite, alien.lasers, True):
                self.lose()
                return
        # Check collision: remove player laser and alien on hit
        pygame.sprite.groupcollide(self.player.sprite.lasers, self.aliens, True, True)
        if not self.aliens:
            self.level_transition(self.level + 1)  # transition to the next level
            return
        self.aliens.draw(screen)
 
        # Draw lasers from all aliens
        for alien in self.aliens:
            alien.lasers.draw(screen)
        self.player.sprite.lasers.draw(screen)  # Draw the player laser
        self.player.draw(screen)
        



    def level_transition(self, level):
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 74)
        level_text = font.render(f"Level: {level}", True, (255, 255, 255))
        level_rect = level_text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(level_text, level_rect)
        pygame.display.flip()
        pygame.time.wait(2000)
        # Clear the level text from screen completely.
        screen.fill((0, 0, 0))
        pygame.display.flip()
        pygame.time.wait(100)  # extra wait to ensure the screen refreshes
        self.level = level  # Update the current level
        self.alien_setup()

        

    def lose(self):
        # Clear screen to black and display "You Lose!" in red.
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 74)
        text = font.render("You Lose!", True, (255, 0, 0))
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text, text_rect)
        pygame.display.flip()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = Game()
    
    # Display level text before player or alien appear
    screen.fill((0, 0, 0))
    font = pygame.font.SysFont(None, 74)
    level_text = font.render("Level: 1", True, (255, 255, 255))
    level_rect = level_text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(level_text, level_rect)
    pygame.display.flip()
    pygame.time.wait(2000)  # wait 2 seconds before starting the game
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))  # Fill the screen with black
        game.run()
        pygame.display.flip()  # Update the display
        clock.tick(60)  # Limit to 60 frames per second