from circleshape import CircleShape
import pygame
from constants import *

class Asteroid(CircleShape):
    containers = None

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.math.Vector2(0, 0)
        if Asteroid.containers:
            for container in Asteroid.containers:
                container.add(self)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (int(self.x), int(self.y)), int(self.radius), 2)
    
    def update(self, dt):
        self.x += self.velocity.x * dt
        self.y += self.velocity.y * dt