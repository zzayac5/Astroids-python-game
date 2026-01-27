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

    score = PLAYER_STARTING_SCORE
#Game Loop#
    while True:
        log_state()
        screen.fill("black")
        updatable.update(dt)
        pygame.font.init()
                
        #Begining the game loop
        
        for asteroid in asteroids:
            if CircleShape.collidees_with(player, asteroid) == True:   #Player runs into asteroid#
                log_event("player_hit")

                player.health -= (ASTEROID_MIN_DAMAGE * asteroid.radius)
                log_event(f"player_health_at{player.health}")

                if player.health < 1:
                    log_event("player_died")
                    print("#########  Game over!  ##########")
                    print("#######  Your Score Is:  ########")
                    print(f"########     {score}     ###########")
                    sys.exit()
                else:
                    continue
            for shot in shots:
                if CircleShape.collidees_with(shot, asteroid) == True:
                    log_event("asteroid_shot")
                    shot.kill()
                    points_earned = SCORE_PER_SHOT // asteroid.radius
                    score += points_earned
                    log_event(f"earned_points {points_earned}")
                    log_event(f"new_score: {score}")
                    if asteroid.health < 1:
                        asteroid.split()
                    else:
                        asteroid.health -= 1
        for drawn in drawable:
            drawn.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60.0) / 1000




if __name__ == "__main__":
    main()
