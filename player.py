import pygame
from circleshape import CircleShape
from constants import *

class Player(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen, color="white", line_width=2):
        # sub-classes must override
        pygame.draw.polygon(screen, color, self.triangle(), line_width)

    def update(self, dt):
        # sub-classes must override
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotation = self.rotate(-1 * dt)
            
        if keys[pygame.K_d]:
            self.rotation = self.rotate(dt)

        if keys[pygame.K_w]:
            self.position = self.move(dt)
            
        if keys[pygame.K_s]:
            self.position = self.move(-1 * dt)
    
    def rotate(self, dt):
        return ( (PLAYER_TURN_SPEED * dt) + self.rotation )
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

        return self.position

