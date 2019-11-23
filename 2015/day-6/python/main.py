import os
import sys
import re

PATH = os.path.join(sys.path[0], '..', 'input')
DATA = open(PATH, 'r').read().split('\n')
PATTERN = r'(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)'

class Grid(object):
    def __init__(self, x, y):
        self.x, self.y = 1000, 1000
        self.grid = [[0 for y in range(self.y)] for x in range(self.x)]

    def read(self, string, type):
        match = re.match(PATTERN, string)
        command = match.group(1)
        x1, y1 = int(match.group(2)), int(match.group(3))
        x2, y2 = int(match.group(4)), int(match.group(5))

        if type == 1:
            self.command1(command, x1, y1, x2, y2)
        elif type == 2:
            self.command2(command, x1, y1, x2, y2)

    def command1(self, command, x1, y1, x2, y2):
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if command == 'turn on':
                    self.grid[x][y] =  1
                elif command == 'turn off':
                    self.grid[x][y] = 0
                elif command == 'toggle':
                    self.grid[x][y] = 0 if self.grid[x][y] else 1


    def command2(self, command, x1, y1, x2, y2):
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if command == 'turn on':
                    self.grid[x][y] +=  1
                elif command == 'turn off':
                    self.grid[x][y] = max(0, self.grid[x][y] - 1)
                elif command == 'toggle':
                    self.grid[x][y] += 2

    def count(self):
        count = 0
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                count += self.grid[x][y]
        return count

def main():
    # Part 1 solution
    p1 = Grid(1000, 1000)
    for line in DATA:
        p1.read(line, 1)
    print(p1.count())

    # Part 2 solution
    p2 = Grid(1000, 1000)
    for line in DATA:
        p2.read(line, 2)
    print(p2.count())

if __name__ == "__main__":
    main()