import os, sys, pyperclip, re

# returns x, y, width, height
def parse(string):
    match = re.search(pattern, string)
    # return int(match[1]), int(match[2]), int(match[3]), int(match[4])
    return list(map(int, [match[i] for i in range(1, 6)]))

# I only later figured out that the dimensions were simply 1000 x 1000
# but this now allows it to be of any dimension
def dimensions(data):
    def bottomright(id, x, y, width, height):
        return (x + width, height + y)    
    bottomrights = list(map(lambda dat : bottomright(*dat), data))
    matrix_x = max(bottomrights, key=lambda item : item[0])[0]
    matrix_y = max(bottomrights, key=lambda item : item[1])[1]
    return matrix_x, matrix_y

path = os.path.join(sys.path[0], '..', 'input')
data = open(path, 'r').read().split('\n')
pattern = r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)'
data = list(map(parse, data))
WIDTH, HEIGHT = dimensions(data)
matrix = [[[set(), 0] for y in range(WIDTH)] for x in range(HEIGHT)]

for id, offset_x, offset_y, width, height in data:
    for x in range(width):
        for y in range(height):
            # matrix[offset_x + x][offset_y + y] = min(2, 1 + matrix[offset_x + x][offset_y + y])
            newX, newY = offset_x + x, offset_y + y
            matrix[newX][newY][1] += 1
            matrix[newX][newY][0].add(id) 

# Checks whether a specific span has any overlaps
def check(offset_x, offset_y, width, height):
    for x in range(width):
        for y in range(height):
            newX, newY = offset_x + x, offset_y + y
            # Quit as soon as the span has been invalidated
            if len(matrix[newX][newY][0]) > 1:
                return False
    return True

# Count all the points in the matrix
count = sum(map(lambda item : len(list(filter(lambda i : i[1] >= 2, item))), matrix))
print(count)

# Checks every id
for dat in data:
    if check(*dat[1:]):
        print(dat[0])
        break