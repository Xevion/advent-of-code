import os
import sys
import re

path = os.path.join(sys.path[0], '..', 'input')
input_ = open(path, 'r').read().split()
orbits = {}

class Mass(object):
    def __init__(self, id_, center):
        self.id = id_
        self.center = center
        self.orbiters = []

    def neighbors(self):
        return self.orbiters + [self.center]

    def countIndirect(self):
        global orbits
        if self.center == "COM":
            return 0
        current = orbits[self.center]
        i = 0
        while current.center != "COM":
            current = orbits[current.center]
            i += 1
        return i + 1

for line in input_:
    central, orbiter = line.split(')')
    orbits[orbiter] = Mass(orbiter, central)

for orbiterID in orbits.keys():
    if orbits[orbiterID].center != "COM":
        orbits[orbits[orbiterID].center].orbiters.append(orbiterID)

# Part 1
print(
    sum(
        orbits[orbiterID].countIndirect() + 1
        for orbiterID in orbits.keys()
    )
)

def find_shortest_path(orbit, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not start in orbit.keys():
            return None
        shortest = None
        for node in orbit[start].neighbors():
            if node not in path:
                newpath = find_shortest_path(orbit, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest

# Part 2
path = find_shortest_path(orbits, orbits["YOU"].center, orbits["SAN"].center)
print(len(path))