# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *


def main():
    # Initializing pygame
    pygame.init()

    # New GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Drawing the game onto the screen
    while True:
        # Check if user has closed the window and exit game if yes
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Creates black screen
        pygame.Surface.fill(screen, (0, 0, 0))
        pygame.display.flip()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
