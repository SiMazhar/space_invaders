import pygame, sys, random
from time import sleep
from player import Player
from aliens import Aliens
from asteroids import Asteroid
from boss import Boss

ASTEROID_SPAWN_EVENT = pygame.USEREVENT + 1

class Game:
    def __init__(self):
        player_sprite = Player((screen_width / 2, screen_height), screen_width, screen_height, 5)
        self.player = pygame.sprite.GroupSingle(player_sprite)

        self.aliens = pygame.sprite.Group()
        self.level = 1  # Initialize the level
        self.alien_setup()
        self.asteroids = pygame.sprite.Group()
        self.boss = pygame.sprite.GroupSingle()

    def asteroid_setup(self):
        a = random.randint(0, 5)
        self.asteroids.add(Asteroid(a))
        num_asteroids = 0
        if self.level == 4:
            num_asteroids = 0
        elif self.level == 8:
            num_asteroids = 0
        for i in range(num_asteroids):
            a = random.randint(0, 2)
            self.asteroids.add(Asteroid(a))


    def alien_setup(self):
        self.aliens.empty()  # clear existing aliens
        if self.level == 1:
            # Level 1: single alien formation
            for row in range(0):
                for column in range(0):
                    x = column * 100 + 50
                    y = row * 50 + 50
                    alien = Aliens(x, y)
                    self.aliens.add(alien)
        elif self.level in (2, 3):
            # For levels 2 and 3: formation with 3 aliens at level 2 and 5 aliens at level 3.
            num_aliens = 0      #1 + 2 * (self.level - 1)
            total_spacing = (num_aliens - 1) * 200  # spacing between aliens is 60 pixels
            start_x = (screen_width - total_spacing) // 2
            y = 50
            for i in range(num_aliens):
                x = start_x + i * 200
                alien = Aliens(x, y)
                self.aliens.add(alien)
        elif self.level in (5, 6):
            # For level 5: 2 rows of five aliens; for level 6: 3 rows of five aliens.
            columns = 0
            rows = 0 if self.level == 5 else 0
            spacing_x = 150  # horizontal spacing between aliens
            spacing_y = 100  # vertical spacing between rows
            start_x = (screen_width - (columns - 1) * spacing_x) // 2
            start_y = 50
            for row in range(rows):
                for col in range(columns):
                    x = start_x + col * spacing_x
                    y = start_y + row * spacing_y
                    alien = Aliens(x, y)
                    self.aliens.add(alien)
        elif self.level == 7:
            # For level 7: formation with 4 rows of five aliens.
            columns = 0
            rows = 0
            spacing_x = 150  # horizontal spacing between aliens
            spacing_y = 100  # vertical spacing between rows
            start_x = (screen_width - (columns - 1) * spacing_x) // 2
            start_y = 50
            for r in range(rows):
                for c in range(columns):
                    x = start_x + c * spacing_x
                    y = start_y + r * spacing_y
                    alien = Aliens(x, y)
                    self.aliens.add(alien)
        elif self.level == 4 or self.level == 8:
            # For level 4: 2 rows of five aliens, but with a different arrangement.
            columns = 0
            rows = 0
            self.asteroid_setup()
            
        elif self.level == 9:
            # For level 9, clear aliens and add the boss.
            self.aliens.empty()
            boss = Boss(screen_width // 2, 50)
            self.boss.add(boss)


    def run(self):
        self.player.update()
        self.aliens.update()  # update aliens using their move function
        self.asteroids.update()
        if self.boss:
            self.boss.update()
        
        # New collision check: if player collides with any asteroid, they lose.
        if pygame.sprite.spritecollide(self.player.sprite, self.asteroids, False):
            self.lose()
            return
        
        if pygame.sprite.spritecollide(self.player.sprite, self.boss, False):
            self.lose()
            return
        
        if pygame.sprite.spritecollide(self.player.sprite, self.aliens, False):
            self.lose()
            return

        # New collision check: if a boss laser touches the player, they lose.
        if self.boss and pygame.sprite.spritecollide(self.player.sprite, self.boss.sprite.lasers, True):
            self.lose()
            return

        # Check if any alien laser hits player.
        for alien in self.aliens:
            if pygame.sprite.spritecollide(self.player.sprite, alien.lasers, True):
                self.lose()
                return

        pygame.sprite.groupcollide(self.player.sprite.lasers, self.aliens, True)
        
        # Boss collision handling: reduce boss health by hits.
        if self.boss:
            hits = pygame.sprite.groupcollide(self.player.sprite.lasers, self.boss, True, False)
            if hits:
                total_hits = sum(len(v) for v in hits.values())
                self.boss.sprite.health -= total_hits
                if self.boss.sprite.health <= 0:
                    self.boss.sprite.kill()
        
        if not self.aliens and not self.asteroids and not self.boss:
            self.level_transition(self.level + 1)
            return
        
        self.aliens.draw(screen)
        if self.boss:
            self.boss.draw(screen)
            self.boss.sprite.lasers.draw(screen)
        for alien in self.aliens:
            alien.lasers.draw(screen)
        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)
        self.asteroids.draw(screen)


        



    def level_transition(self, level):
        screen.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 74)
        if level == 10:
            win_text = font.render("You Win!", True, (0, 255, 0))
            win_rect = win_text.get_rect(center=(screen_width // 2, screen_height // 2))
            screen.blit(win_text, win_rect)
            pygame.display.flip()
            pygame.time.wait(2000)
            pygame.quit()
            sys.exit()
        else:
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

    # schedule ASTEROID_SPAWN_EVENT every 200 ms
    pygame.time.set_timer(ASTEROID_SPAWN_EVENT, 200)
    # remember when we started spawning
    spawn_start = pygame.time.get_ticks()
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        screen.fill((0, 0, 0))  # Fill the screen with black
        game.run()
        pygame.display.flip()  # Update the display
        clock.tick(60)  # Limit the frame rate to 60 FPS