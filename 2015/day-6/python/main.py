import os
import sys
import re

PATH = os.path.join(sys.path[0], '..', 'input')
DATA = open(PATH, 'r').read().split('\n')
PATTERN = r'(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)'

class Grid(object):
    def __init__(self, x, y):
        self.x, self.y = 1000, 1000
        self.boolgrid = [[False for y in range(self.y)] for x in range(self.x)]

    def read(self, string):
        match = re.match(PATTERN, string)
        command = match.group(1)
        x1, y1 = int(match.group(2)), int(match.group(3))
        x2, y2 = int(match.group(4)), int(match.group(5))
        self.command(command, x1, y1, x2, y2)

    def command(self, command, x1, y1, x2, y2):
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if command == 'turn on':
                    self.boolgrid[x][y] = True
                elif command == 'turn off':
                    self.boolgrid[x][y] = False
                elif command == 'toggle':
                    self.boolgrid[x][y] = not self.boolgrid[x][y]

    def count(self):
        count = 0
        for x in range(len(self.boolgrid)):
            for y in range(len(self.boolgrid[x])):
                count += 1 if self.boolgrid[x][y] else 0
        return count

def main():
    grid = Grid(1000, 1000)
    for line in DATA:
        grid.read(line)
    print(grid.count())

if __name__ == "__main__":
    main()
    # grid = Grid(1000, 1000)
    # grid.command('turn on', 0, 0, 2, 2)
    # print(grid.count())