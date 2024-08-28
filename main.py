# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from player import Player


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

    x = int(SCREEN_WIDTH / 2)
    y = int(SCREEN_HEIGHT / 2)
    player1 = Player(x, y)

    # Drawing the game onto the screen
    while True:

        # Check if user has closed the window and exit game if yes
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Creates black screen
        pygame.Surface.fill(screen, (0, 0, 0))
        # Render the player on the screen
        player1.draw(screen)
        player1.update(dt)

        # Updates the display
        pygame.display.flip()

        # Pause the game loop until 1/60th of a second has passed
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
