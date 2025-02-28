import pygame
import sys
from constants import *
from player import Player
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)

    asteroid_field = AsteroidField()

    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updateable.update(dt) 
        for obj in asteroids:
            if obj.collision(player):
                sys.exit("Game Over, Loser!!!")
        
        for obj in shots:
            for obja in asteroids:
                if obj.collision(obja):
                    obj.kill()
                    obja.split()


        screen.fill("black")
        #player.draw(screen)
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        #player.update(dt)
        # print(dt) -- debug only

if __name__ == "__main__":
    main()
