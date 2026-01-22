import pygame
from constants import * 
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
import sys
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

# General Groups#
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

# Asteroid Setup #
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)

# Asteroid Field Setup #
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

# Player Setup #
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

# Shooting Setup #
    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    
    



#Game Loop#
    while True:
        log_state()
        screen.fill("black")
        updatable.update(dt)
        for asteroid in asteroids:
            if CircleShape.collidees_with(player, asteroid) == True:
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for drawn in drawable:
            drawn.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60.0) / 1000



    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")





if __name__ == "__main__":
    main()
