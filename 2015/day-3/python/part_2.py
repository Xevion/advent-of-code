import os
import sys

from collections import defaultdict
from itertools import cycle

PATH = os.path.join(sys.path[0], '..', 'input')
DATA = '--' + open(PATH).read()

def UP(santa): santa[1] += 1
def DOWN(santa): santa[1] -= 1
def RIGHT(santa): santa[0] += 1
def LEFT(santa): santa[0] -= 1

DIRECTIONS = {'^' : UP, '<' : LEFT, '>' : RIGHT, 'v' : DOWN, '-' : lambda *args : None}

humanSanta = [0, 0]
roboSanta = [0, 0]
houses = defaultdict(int)
cycleIter = cycle(range(2))

for direction in DATA:
    alternate = next(cycleIter)
    
    if bool(alternate):
        DIRECTIONS[direction](roboSanta)
        houses[f'{roboSanta[0]},{roboSanta[1]}'] += 1
    else:
        DIRECTIONS[direction](humanSanta)        
        houses[f'{humanSanta[0]},{humanSanta[1]}'] += 1

print(len(list(v for v in houses.values() if v >= 1)))