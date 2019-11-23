import os
import sys

PATH = os.path.join(sys.path[0], '..', 'input')
DATA = open(PATH).read()

print(DATA.count('(') - DATA.count(')'))

level = 0
for i, char in enumerate(DATA):
    level += 1 if char == '(' else -1
    if level == -1:
        print(i + 1)
        break