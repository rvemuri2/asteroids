from circleshape import *
import pygame
from constants import *
class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, screen, x, y, radius, width=2):
        pygame.draw.circle(screen, "white", (x, y), radius, width)
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(-dt)
        if keys[pygame.K_s]:
            self.move(dt)