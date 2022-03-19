import pygame
import Food
import math
from AI import Creature


class Animal(Creature):
    def __init__(self, x, y, surface, color, nodes):
        self.MAX_SPEED = 50
        self.x = x
        self.y = y
        self.surface = surface
        self.color = color
        Creature.__init__(self, 2, 2, nodes)

    def draw(self):
        pygame.draw.circle(self.surface, self.color, [self.x, self.y], 20)

    def update(self):
        pass



class Herbivore(Animal):
    def __init__(self, x, y, surface, nodes):
        Animal.__init__(self, x, y, surface, [150, 150, 20], nodes)

    def getNearestBerry(self, berries):
        nearest = None
        for b in berries:
            if(b.getdistance() < nearest.getdistance()):
                nearest = b
        return nearest

    def move(self, speed, angle):
        speed = abs(speed)
        if speed > self.MAX_SPEED:
            speed = self.MAX_SPEED
        self.x += speed * math.cos((math.pi/180) * angle)
        self.y += speed * math.sin((math.pi / 180) * angle)

    def update(self, berries):
        target = self.getNearestBerry(berries)
        self.inputs.push(target.getdistance(self.x, self.y))
        self.inputs.push(target.getangleto(self.x, self.y))
        self.process()
        self.move(self.outputs.pop(), self.outputs.pop())