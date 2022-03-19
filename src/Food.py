import pygame
from math import *


class Berry:
    def __init__(self, x, y, surface):
        self.x = x
        self.y = y
        self.surface = surface
        self.eaten = False

    def draw(self):
        pygame.draw.circle(self.surface, [255, 0, 0], [self.x, self.y], 5)

    def getdistance(self, x, y):
        return sqrt(pow(abs(self.x - x), 2) + pow(abs(self.y - y), 2))

    def getangleto(self, x, y):
        return atan2(self.y - y, self.x - x)

    def eat(self):
        self.eaten = True
