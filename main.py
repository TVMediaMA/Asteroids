import pygame
from constants import *
from player import Player

def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Set up the clock
    clock = pygame.time.Clock()
    dt = 0

    # Instantiate the player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Draw the player
        player.draw(screen)

        # Cap the frame rate
        dt = clock.tick(60) / 1000.0

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
