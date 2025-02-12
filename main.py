import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    Shot.containers = (shots, updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        
        updatable.update(dt)
        
        screen.fill((0,0,0))

        for obj in drawable:
            obj.draw(screen)

        for obj in asteroids:
            collision = obj.check_collision(player)
            
            for shot in shots:
                if obj.check_collision(shot):
                    obj.split()
                    shot.kill()

            if collision:
                print("Game over!")
                return
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()