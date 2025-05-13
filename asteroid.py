import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid (CircleShape):
    containers = None
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)
    
    def split(self):
        self.kill()
        # Create two smaller asteroids
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            velocity_angle1 = self.velocity.rotate(random_angle) * ASTEROID_SPLIT_SPEED
            velocity_angle2 = self.velocity.rotate(-random_angle) * ASTEROID_SPLIT_SPEED
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid1.velocity = velocity_angle1
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2.velocity = velocity_angle2
   
    def update(self, dt):
        self.position += self.velocity * dt
        
