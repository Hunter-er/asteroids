import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen, color="white", width=2):
        # sub-classes must override
        pygame.draw.circle(screen, color, self.position, self.radius, width)

    def update(self, dt):
        # sub-classes must override
        self.position += (self.velocity * dt)