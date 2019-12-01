import os
import sys
import math

PATH = os.path.join(sys.path[0], '..', 'input')
DATA = list(map(int, open(PATH, 'r').readlines()))

BASIC_FUEL = lambda mass : math.floor(mass / 3) - 2
ADVANCED_FUEL = lambda mass : BASIC_FUEL(mass) + (BASIC_FUEL(BASIC_FUEL(mass)) if BASIC_FUEL(mass) > 0 else 0)

# def ADVANCED_FUEL(mass):
#     total = 0
#     while mass > 0:
#         mass = BASIC_FUEL(mass)
#         total += mass if mass >= 0 else 0 
#     return total

print(sum(map(BASIC_FUEL, DATA)))
print(sum(map(ADVANCED_FUEL, DATA)))