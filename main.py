import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import AsteroidField
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, "black")

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip() 
        
        dt = clock.tick(60)/1000

        for sprite in updatable:
            sprite.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collisions(player):
                print("Game Over!")
                sys.exit()


if __name__ == "__main__":
    main()