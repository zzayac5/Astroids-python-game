import pygame
from circleshape import CircleShape
from constants import *
from logger import log_event
import random



class Asteroid (CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        if self.radius <= ASTEROID_MIN_RADIUS * 1:
            color = SMALL_ASTEROID_COLOR
        elif self.radius >= ASTEROID_MIN_RADIUS *1.15 and self.radius <= ASTEROID_MIN_RADIUS * 2.9:
            color = MED_ASTEROID_COLOR
        else:
            color = LARGE_ASTEROID_COLOR
        pygame.draw.circle(screen, color, self.position, self.radius, LINE_WIDTH)
        

    def update(self, dt):
        self.position += (self.velocity * dt)

    def drop_power_up(self):
        pass

    def split (self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_asteroid_angle = random.uniform(20, 50)
            new_asteroid_num_one_vector = self.velocity.rotate(new_asteroid_angle)
            new_asteroid_num_two_vector = self.velocity.rotate(- new_asteroid_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_1.velocity = new_asteroid_num_one_vector * 1.2
            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2.velocity = new_asteroid_num_two_vector * 1.2
    

