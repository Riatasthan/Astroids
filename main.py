# Importing module
import pygame

# Imporitng constants from constants file
from constants import *

# Main loop
def main():
    # Initalising the module
    pygame.init()
    # Setting screen size 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Calls an infinte loop for a screen, and enables close/minimise button on pygame screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()
    #Start up text
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")



if __name__ == "__main__":
    main()