import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    run_game = True

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    player_x_init = SCREEN_WIDTH // 2
    player_y_init = SCREEN_HEIGHT // 2
    player = Player(player_x_init, player_y_init, PLAYER_RADIUS)
    asteroid_field = AsteroidField()

    while run_game:
        screen.fill("black")

        updatable.update(dt)
        for drawable_object in drawable:
            drawable_object.draw(screen)
        for asteroid in asteroids:
            asteroid.draw(screen)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
    