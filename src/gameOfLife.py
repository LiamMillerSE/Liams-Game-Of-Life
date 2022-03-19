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
    animals.append(Genetics.GenerateFullspeedHerbivore(250, 250, pygame.display.get_surface()))
    animals.append(Genetics.GenerateFastCarnavore(0, 0, pygame.display.get_surface()))
    #for i in range(0, 30):
    #    berries.append(Berry(random.randint(0, 500), random.randint(0, 500), pygame.display.get_surface()))
    berries.append(Berry(400, 400, pygame.display.get_surface()))
    berries.append(Berry(100, 400, pygame.display.get_surface()))
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
            elif isinstance(a, (type, Carnivore)):
                a.update([a for a in animals if isinstance(a, (type, Herbivore))])
            else:
                a.update()
            a.draw()
        for f in berries:
            f.draw()
        berries = [b for b in berries if not b.eaten]
        animals = [a for a in animals if not a.eaten]
        pygame.display.flip()
        time.sleep(0.1)


gameOfLife()
