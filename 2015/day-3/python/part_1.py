import os
import sys

from collections import defaultdict

PATH = os.path.join(sys.path[0], '..', 'input')
DATA = open(PATH).read()

pos = [0, 0]

def UP():
    pos[1] += 1

def DOWN():
    pos[1] -= 1
def RIGHT():
    pos[0] += 1
def LEFT():
    pos[0] -= 1

DIRECTIONS = {'^' : UP, '<' : LEFT, '>' : RIGHT, 'v' : DOWN}

houses = defaultdict(int)
for direction in DATA:
    DIRECTIONS[direction]()
    houses[f'{pos[0]},{pos[1]}'] += 1

print(len(list(v for v in houses.values() if v >= 1)))