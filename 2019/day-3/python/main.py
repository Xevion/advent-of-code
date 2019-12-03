import os
import sys

PATH = os.path.join(sys.path[0], '..', 'input')
DATA = [line for line in open(PATH, 'r').readlines()]

class Flag(object):
    def __init__(self, o=False, t=False):
        self.first = o
        self.second = t
        
        self.fstep = -1
        self.sstep = -1

    def mark(self, f, step):
        if f == 0 and self.fstep == -1:
            self.fstep = step
        elif f == 1 and self.sstep == -1:
            self.sstep = step


    @property
    def intersect(self):
        return self.first and self.second

synth = lambda pos : f'{pos[0]},{pos[1]}'
grid = {}
offsets = {
    'L' : (-1, 0),
    'R' : (1, 0),
    'U' : (0, 1),
    'D' : (0, -1)
}

for f, line in enumerate(DATA):
    curpos = [0, 0]
    step = 0

    for command in line.split(','):
        offset = offsets[command[0]]
        magnitude = int(command[1:])

        for y in range(1, magnitude + 1):
            step += 1
            curpos[0] += offset[0]
            curpos[1] += offset[1]
            key = synth(curpos)

            if key in grid.keys():
                if f == 0:
                    grid[key].first = True
                elif f == 1:
                    grid[key].second = True
                grid[key].mark(f, step)
            else:
                grid[key] = Flag(o=True) if f == 0 else Flag(t=True)
                grid[key].mark(f, step)

# Part 1
manhattan = lambda d : sum(abs(int(n)) for n in d.split(','))
select = list(filter(lambda item : grid[item].intersect, grid.keys()))
select = list(map(manhattan, select))
print(min(select))

# Part 2
combo = lambda x : grid[x].fstep + grid[x].sstep
found = list(filter(lambda item : grid[item].intersect, grid.keys()))
found = list(map(combo, found))
print(min(found))