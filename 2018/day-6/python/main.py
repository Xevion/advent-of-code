import os, sys, collections

path = os.path.join(sys.path[0], '..', 'input')
# data = open(path, 'r').read().split('\n')
data = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9""".split('\n')
points = list(map(lambda item : [int(num.strip()) for num in item.split(', ')], data))

def manhattan(pos1, pos2):
    return abs(pos2[0] - pos1[0]) + abs(pos2[1] - pos1[1])

def closest(pos):
    return min(points, key=lambda point : manhattan(point, pos))


grid = collections.defaultdict(dict)
scores = collections.defaultdict(dict)
for pos in points:
    scores[pos[0]][pos[1]] = 0
ensure = 500
for x in range(-ensure, ensure):
    for y in range(-ensure, ensure):
        pos = closest((x, y))
        # grid[x][y] = pos
        scores[pos[0]][pos[1]] += 1

from pprint import pprint
# pprint(scores)
true_scores = []
for x, yy in scores.items():
    for y, score in yy.items():
        true_scores.append(("({}, {}) : {}".format(x, y, score), score))
true_scores.sort(key=lambda item : item[1])
pprint([score[0] for score in true_scores])