# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from asteroidfield import AsteroidField
from constants import *
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initializing pygame
    pygame.init()

    # New GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Setting FPS
    clock = pygame.time.Clock()
    dt = 0

    # Assigning groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    # Creating player in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Creating the asteroid field
    asteroidfield = AsteroidField()

    # Drawing the game onto the screen
    while True:

        # Check if user has closed the window and exit game if yes
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Creates black screen
        pygame.Surface.fill(screen, (0, 0, 0))

        # Render the player on the screen
        for thing in updatable:
            thing.update(dt)
        for thing in drawable:
            thing.draw(screen)

        # Updates the display
        pygame.display.flip()

        # Pause the game loop until 1/60th of a second has passed
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
