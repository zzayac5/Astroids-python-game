from constants import *
import pygame
from circleshape import CircleShape



class Shot(CircleShape):
    def __init__(self, x, y, status):
        if status == PLAYER_STATUS_POWER_UP:
            radius = SHOT_RADIUS * SHOT_POWERUP_NORMAL
            color = "red"
        elif status == PLAYER_STATUS_POWER_MAX:
            radius = SHOT_RADIUS * SHOT_POWERUP_MAX
            color = "purple"
        else:
            radius = SHOT_RADIUS
            color = "white"
        super().__init__(x, y, radius)
        self.status = status
        self.color = color
        



    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, LINE_WIDTH)
            

        

    def update(self,dt):
        self.position += (self.velocity * dt)

