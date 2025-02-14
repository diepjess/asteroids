# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *


def main():
    pygame.init()
    game_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # fill screen with color
        game_screen.fill("black")
        
        # flip() the display to refresh screen
        pygame.display.flip()


if __name__ == "__main__":
    main()