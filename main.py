# Import sys
import sys

# Importing module
import pygame

# Imporitng constants from constants file
from constants import *

# imports player from Player file
from player import Player

# inports asteriod
from asteroid import Asteroid

# imports asteriod field
from asteriodfield import AsteroidField

from shot import Shot

# Main loop
def main():
    # Initalising the module
    pygame.init()
    # Setting screen size 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Clock and delta time
    clock = pygame.time.Clock()
  

    # Create groups for objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    asteriod_field = AsteroidField()
    
    
    Player.containers = (updatable, drawable)
   
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

   # Calls an infinte loop for a screen, and enables close/minimise button on pygame screen, game over
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        for asteriod in asteroids:
            if asteriod.collides_with(player):
                print("Game over!")
                sys.exit()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
    
    #Limits FPS
        dt = clock.tick(60) / 1000
    
    #Start up text
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")



if __name__ == "__main__":
    main()