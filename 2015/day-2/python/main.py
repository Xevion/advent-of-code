import os
import sys

PATH = os.path.join(sys.path[0], '..', 'input')
DATA = open(PATH).readlines()

paper = 0
ribbon = 0

for line in DATA:
    l, w, h = list(map(int, line.split('x')))
    
    areas = [l*w, w*h, h*l]
    volume = l*w*h
    perimeters = [2*(l+w), 2*(h+w), 2*(h+l)]
    areas.extend(areas)

    paper += sum(areas) + min(areas)
    ribbon += min(perimeters) + volume

print(paper)
print(ribbon)