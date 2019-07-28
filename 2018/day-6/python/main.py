import os, sys, collections

path = os.path.join(sys.path[0], '..', 'input')
data = open(path, 'r').read().split('\n')
# data = """1, 1
# 1, 6
# 8, 3
# 3, 4
# 5, 5
# 8, 9
# 18, 10""".split('\n')
points = list(map(lambda item : tuple((int(num.strip()) for num in item.split(', '))), data))

def dist(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

is_infinite = set()
counts = collections.defaultdict(int)

minx, miny = min(x for x,y in points), min(y for x,y in points)
maxx, maxy = max(x for x,y in points), max(y for x,y in points)

for y in range(miny, maxy + 1):
    for x in range(minx, maxx + 1):
        
        distances = [ (dist((x, y), point), i) for i, point in enumerate(points)]
        distances.sort()

        if distances[0][0] != distances[1][0]:
            counts[distances[0][1]] += 1

            if x == minx or x == maxx or y == miny or y == maxy:
                is_infinite.add(distances[0][1])

for k in is_infinite:
    counts.pop(k)

a2 = 0
for x in range(minx, maxx + 1):
    for y in range(miny, maxy + 1):
        sumdist = sum(dist((x, y), point) for point in points)
        a2 += 1 if sumdist < 10_000 else 0

a1 = max(counts.items(), key=lambda item : item[1])
a1 = a1, points[a1[0]]
print('Point {} had the largest non-infinite area at {} spaces.'.format(a1[1], a1[0][1]))
print('There are {} spaces with a distance < 10,000 to all given coordinates.'.format(a2))