import os, sys

path = os.path.join(sys.path[0], 'input')
data = list(open(path, 'r').read())

w, h = 25, 6

# Part 1
layers = []
while len(data) > 0:
    layer = []
    for row in range(h):
        row = [data.pop(0) for _ in range(w)]
        layer.append(list(map(int, row)))
    layers.append(layer)

count = lambda layer, n = 0: sum(row.count(n) for row in layer)
layer_select = min(layers, key=count)
print(sum(r.count(1) for r in layer_select) * sum(r.count(2) for r in layer_select))

# Part 2
def determine(pixels):
    cur = pixels[0]
    for pixel in pixels[1:]:
        cur = pixel if pixel == 0 or pixel == 1 else cur
    return cur

getPixels = lambda ly, x, y : [l[y][x] for l in ly]
pixels = [[getPixels(layers, x, y) for x in range(w)] for y in range(h)]
pixels  = [[determine(cell[::-1]) for cell in row] for row in pixels]
print('\n'.join(''.join('#' if bool(cell) else ' ' for cell in row) for row in pixels))