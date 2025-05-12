import pygame
from constants import *

def main():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Update the display
        pygame.display.flip()
        
        # Handle game logic here

if __name__ == "__main__":
    main()