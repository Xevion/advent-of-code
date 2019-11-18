import re
import os
import sys
import time

import numpy as np
import matplotlib.pyplot as plt


# Constants

RE_PATTERN = r"position=<\s*(\-*\d+),\s*(\-*\d+)> velocity=<([-*\s?]\d+), ([-?\s?]\d+)>"
PATH = os.path.join(sys.path[0], '..', 'input')

getX = lambda p : p.pos[0]
getY = lambda p : p.pos[1]

# MovingPoint (pos, velocity) class

class MovingPoint(object):
    def __init__(self, input):
        match = re.search(RE_PATTERN, input)
        self.pos = [int(match.group(1)), int(match.group(2))]
        self.vel = [int(match.group(3)), int(match.group(4))]

    def simulate(self, t=1):
        self.pos[0] += self.vel[0] * t
        self.pos[1] += self.vel[1] * t

    def __repr__(self):
        return f"<MovingPoint pos({self.pos[0]}, {self.pos[1]}) vel({self.vel[0]}, {self.vel[1]})"


# Matrix class for managing a list of points and quickly running simulation
class Matrix(object):
    def __init__(self, input):
        self.points = []
        for line in input.readlines():
            self.points.append(MovingPoint(line))
        input.close()
    
    def simulate(self, t=1):
        for point in self.points:
            point.simulate(t)

    @property
    def minX(self):
        return min(self.points, key=lambda p : p.pos[0]).pos[0]
    
    @property
    def maxX(self):
        return max(self.points, key=lambda p : p.pos[0]).pos[0]
    
    @property
    def minY(self):
        return min(self.points, key=lambda p : p.pos[1]).pos[1]

    @property
    def maxY(self):
        return max(self.points, key=lambda p : p.pos[1]).pos[1]

    @property
    def Xs(self):
        return [p.pos[0] for p in self.points]

    @property
    def Ys(self):
        return [p.pos[1] for p in self.points]

import copy

print('Building Matrix')
original = Matrix(open(PATH, 'r'))
matrix = copy.deepcopy(original)
difs = []
print('Matrix built, copy made.')

# Simulate all likely points in time of message
print('Simulating')
t1 = time.time()
for i in range(11000):
    difX = abs(matrix.maxX - matrix.minX)
    difY = abs(matrix.maxY - matrix.minY)
    difs.append(difX + difY)
    matrix.simulate(1)
t2 = time.time()
print(f'Simulated in {round(t2 - t1, 2)} seconds')

# Point in time where all points are closest
best = min(list(enumerate(difs)), key=lambda x:x[1])
print(f'Found best point {best[0]} seconds in the future.')

print('Resimulating')
original.simulate(best[0])
print('Building Scatter Plot')
plt.scatter(original.Xs, original.Ys)
plt.gca().invert_yaxis()
plt.show()