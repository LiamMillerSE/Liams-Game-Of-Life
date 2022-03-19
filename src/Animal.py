import pygame
import Food
from math import *
from AI import Creature


class Animal(Creature):
    def __init__(self, x, y, surface, color, nodes):
        self.MAX_SPEED = 50
        self.MAX_EAT_RADIUS = 10
        self.x = x
        self.y = y
        self.surface = surface
        self.color = color
        self.eaten = False
        Creature.__init__(self, 2, 2, nodes)

    def draw(self):
        pygame.draw.circle(self.surface, self.color, [self.x, self.y], 20)

    def getdistance(self, x, y):
        return sqrt(pow(abs(self.x - x), 2) + pow(abs(self.y - y), 2))

    def getangleto(self, x, y):
        return atan2(self.y - y, self.x - x)

    def move(self, speed, angle):
        # compensate speed
        speed = abs(speed)
        if speed > self.MAX_SPEED:
            speed = self.MAX_SPEED
        self.x += speed * cos(angle)
        self.y += speed * sin(angle)
        # keep in bounds
        if self.x < 0:
            self.x = 0
        elif self.x > self.surface.get_size()[0]:
            self.x = self.surface.get_size()[0]
        if self.y < 0:
            self.y = 0
        elif self.y > self.surface.get_size()[1]:
            self.y = self.surface.get_size()[1]

    def update(self):
        pass

    def eat(self):
        self.eaten = True


class Herbivore(Animal):
    def __init__(self, x, y, surface, nodes):
        Animal.__init__(self, x, y, surface, [51, 25, 0], nodes)

    def getNearestBerry(self, berries):
        if len(berries) <= 0:
            return None
        nearest = berries[0]
        for b in berries:
            if b.getdistance(self.x, self.y) < nearest.getdistance(self.x, self.y):
                nearest = b
        return nearest

    def update(self, berries):
        target = self.getNearestBerry(berries)
        if target is not None:
            self.inputs.append(target.getdistance(self.x, self.y))
            self.inputs.append(target.getangleto(self.x, self.y))
            self.process()
            self.move(self.outputs.pop(0), self.outputs.pop(0))
            if target.getdistance(self.x, self.y) <= self.MAX_EAT_RADIUS:
                target.eat()
        Animal.update(self)

class Carnivore(Animal):
    def __init__(self, x, y, surface, nodes):
        Animal.__init__(self, x, y, surface, [255, 128, 0], nodes)

    def getNearestHerbivore(self, herbivores):
        if len(herbivores) <= 0:
            return None
        nearest = herbivores[0]
        for b in herbivores:
            if b.getdistance(self.x, self.y) < nearest.getdistance(self.x, self.y):
                nearest = b
        return nearest

    def update(self, herbovires):
        target = self.getNearestHerbivore(herbovires)
        if target is not None:
            self.inputs.append(target.getdistance(self.x, self.y))
            self.inputs.append(target.getangleto(self.x, self.y))
            self.process()
            self.move(self.outputs.pop(0), self.outputs.pop(0))
            if target.getdistance(self.x, self.y) <= self.MAX_EAT_RADIUS:
                target.eat()
        Animal.update(self)
