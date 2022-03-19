import random

import pygame
import sys
import time
from Food import Berry
from Animal import *
import Genetics

def gameOfLife():
    # Set up Window
    pygame.init()
    size = width, height = 500, 500
    window = pygame.display.set_mode(size)
    berries = []
    animals = []

    #create test animal
    animals.append(Genetics.GenerateStraightthroughHerbivore(20, 20, pygame.display.get_surface(), [240, 100, 100]))
    for i in range(0, 30):
        berries.append(Berry(random.randint(0, 500), random.randint(0, 500), pygame.display.get_surface()))
    # Game Loop
    while 1:
        # see if the game is exiting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # paint the screen
        window.fill([50, 100, 50])
        for a in animals:
            if isinstance(a, (type, Herbivore)):
                a.update(berries)
            else:
                a.update()
            a.draw()
        for f in berries:
            f.draw()
        pygame.display.flip()
        time.sleep(0.05)


gameOfLife()
