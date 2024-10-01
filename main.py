import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import AsteroidField
from shot import *
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    counter, text = 60, '60'.rjust(1)
    score_counter = 0
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    while True:
        for event in pygame.event.get():

            if(event.type == pygame.USEREVENT):
                if counter > 0:
                    text = "Time: " + str(counter).rjust(1)
                else:
                    print("Time's Up!")
                    print("Game Score:", score_counter)
                    sys.exit()
                counter -= 1

            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, "black")
        label = font.render(text, 1, (255, 0, 0))
        score_label = font.render(f'Score: {score_counter}', True, (0, 255, 0))
        screen.blit(score_label, (1100, 50))
        screen.blit(label, (40, 50))

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip() 
        
        dt = clock.tick(60)/1000

        for sprite in updatable:
            sprite.update(dt)
        
        for asteroid in asteroids:
            if asteroid.collisions(player):
                print("Game Over!")
                print("Game Score:", score_counter)
                sys.exit()
            for bullet in shots:
                if(asteroid.collisions(bullet)):
                    score_counter += 1
                    asteroid.split()
                    bullet.kill()



if __name__ == "__main__":
    main()