import os, sys, collections

path = os.path.join(sys.path[0], '..', 'input')
data = open(path, 'r').read().split('\n')
data = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9
18, 10""".split('\n')
points = list(map(lambda item : tuple((int(num.strip()) for num in item.split(', '))), data))

def manhattan(pos1, pos2):
    return abs(pos2[0] - pos1[0]) + abs(pos2[1] - pos1[1])

def closest(pos):
    return min(points, key=lambda point : manhattan(point, pos))

def edgeCoords(x1, y1, x2, y2):
    coords = []
    x1, x2 = (x1, x2) if x1 < x2 else (x2, x1)
    y1, y2 = (y1, y2) if y1 < y2 else (y2, y1)
    for x in range(x1, x2+1):
        coords.append((x1 + x, y1))
        coords.append((x1 + x, y2))
    for y in range(y1, y2+1):
        coords.append((x1, y1 + y))
        coords.append((x2, y1 + y))
    return coords

def get_id(pos):
    return f"{pos[0]},{pos[1]}"
def get_pos(id):
    id = id.split(',')
    return (id[0], id[1])

def getDimensions(points):
    zippoints = list(zip(*points))
    minx, miny = min(zippoints[0]), min(zippoints[1])
    maxx, maxy = max(zippoints[0]), max(zippoints[1])
    return minx, miny, maxx, maxy

def formatted(edges, points, size=None):
    if not size:
        size = max(*getDimensions(points)) + 3
    grid = [[' # ' if (x, y) in edges else ' ? ' if (x, y) in points else ' . ' for y in range(size)] for x in range(size)]
    return '\n'.join([''.join(row) for row in grid])

from pprint import pprint
# marked = {get_id(pos) : False for pos in points}
marked = collections.defaultdict(int)
minx, miny, maxx, maxy = getDimensions(points)
minx, miny, maxx, maxy = minx - 1, miny - 1, maxx + 1, maxy + 1
edges = edgeCoords(minx, miny, maxx, maxy)
for edge in edges:
    close = closest(edge)
    marked[get_id(close)] += True
# pprint(marked)

scores = collections.defaultdict(int)
for x in range(minx, maxx):
    for y in range(miny, maxy):
        close = closest((x, y))
        scores[get_id(close)] += 1

print(scores)
for id in scores.keys():
    if id in marked:
        continue
    print(id, scores[id])
best = max(scores.items(), key=lambda item : 0 if item[0] in marked else item[1])
print(best)
# print(formatted(edges=edgeCoords(minx, miny, maxx, maxy), points=points))