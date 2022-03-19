from AI import *
from Animal import *


def GenerateStraightthroughHerbivore(x, y, surface):
    return Herbivore(x, y, surface, [StraightThrough(), StraightThrough()])

def GenerateFullspeedHerbivore(x, y, surface):
    return Herbivore(x, y, surface, [Maximize(10), StraightThrough()])

def GenerateFastCarnavore(x, y, surface):
    return Carnivore(x, y, surface, [Maximize(15), StraightThrough()])
