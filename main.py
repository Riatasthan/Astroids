# Importing module
import pygame

# Initalising the module
pygame.init()

# Imporitng constants from constants file
from constants import *

# Setting screen size 
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

while True:
    pygame.Surface.fill(screen, (0, 255, 0))

# Main loop
def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()