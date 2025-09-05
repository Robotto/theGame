import pygame
import sys

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

PLAYER_SIZE = 50
PLAYER_SPEED = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (200, 50, 50)
BLUE  = (50, 50, 200)

# --- Player class ---
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, color, controls):
        super().__init__()
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.controls = controls
        self.speed = PLAYER_SPEED

    def update(self, pressed_keys):
        if pressed_keys[self.controls["up"]]:
            self.rect.y -= self.speed
        if pressed_keys[self.controls["down"]]:
            self.rect.y += self.speed
        if pressed_keys[self.controls["left"]]:
            self.rect.x -= self.speed
        if pressed_keys[self.controls["right"]]:
            self.rect.x += self.speed

        # Keep inside screen bounds
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - PLAYER_SIZE))
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - PLAYER_SIZE))


# --- Main game function ---
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Local Multiplayer Boilerplate")
    clock = pygame.time.Clock()

    # Define controls for players
    controls_p1 = {"up": pygame.K_w, "down": pygame.K_s,
                   "left": pygame.K_a, "right": pygame.K_d}
    controls_p2 = {"up": pygame.K_UP, "down": pygame.K_DOWN,
                   "left": pygame.K_LEFT, "right": pygame.K_RIGHT}

    # Create players
    player1 = Player(200, 300, RED, controls_p1)
    player2 = Player(600, 300, BLUE, controls_p2)

    all_sprites = pygame.sprite.Group(player1, player2)

    # Game loop
    while True:
        # --- Event handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # --- Update ---
        pressed_keys = pygame.key.get_pressed()
        all_sprites.update(pressed_keys)

        # Example collision check
        if player1.rect.colliderect(player2.rect):
            print("Collision!")

        # --- Draw ---
        screen.fill(WHITE)
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
