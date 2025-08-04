import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, position, radius, velocity):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.radius = radius
        self.velocity = velocity
        self.position = position

    def draw(self, screen, color="white", width=2):
        # sub-classes must override
        pygame.draw.circle(screen, color, self.position, self.radius, width)

    def update(self, dt):
        # sub-classes must override
        self.position += (self.velocity * dt)