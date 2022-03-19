from AI import *
from Animal import *


def GenerateStraightthroughHerbivore(x, y, surface, color):
    return Herbivore(x, y, surface, [StraightThrough(), StraightThrough()])
