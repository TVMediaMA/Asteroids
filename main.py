import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Shot

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

    # Add Groups for updating and drawing
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    # Add the player to the updatable and drawable groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (bullets, updatable, drawable)

    # Instantiate the player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, bullets)
    asteroid_field = AsteroidField()

    # Main game loop
    while True:
        if player.timer > 0:
            player.timer -= dt
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        # Handle key events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Check if the player can shoot
                    if player.timer <= 0:
                        # Reset the timer
                        player.timer = 0.3
                        # Create a new shot and add it to the bullets group
                        shot = player.shoot()
                        bullets.add(shot)
                    else:
                        # If the timer is not up, do not shoot
                        print("Cannot shoot yet!")
                  
                    # Check for collision with asteroids

        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Move all
        updatable.update(dt)

        # Draw all
        for sprite in drawable:
            sprite.draw(screen)

        for shape in asteroids:
            if player.collide(shape):
                print("Game over!")
                pygame.quit()
                return

        # Cap the frame rate
        dt = clock.tick(60) / 1000.0

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":    main()
