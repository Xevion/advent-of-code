import os
import sys

PATH = os.path.join(sys.path[0], '..', 'input')
orig = list(map(int, open(PATH, 'r').read().split(',')))

def calculate(noun, verb):
    arr = orig.copy()
    arr[1] = noun
    arr[2] = verb
    curpos = 0
    while curpos < len(arr):
        if arr[curpos] == 1:
            arr[arr[curpos + 3]] = arr[arr[curpos + 1]] + arr[arr[curpos + 2]]
        elif arr[curpos] == 2:
            arr[arr[curpos + 3]] = arr[arr[curpos + 1]] * arr[arr[curpos + 2]]
        elif arr[curpos] == 99:
            # print(f'Stopped at {curpos}')
            break
        curpos += 4
    return arr[0]

print(calculate(12, 2))

for noun in range(0, 100):
    for verb in range(0, 100):
        if calculate(noun, verb) == 19690720:
            print(100 *  noun + verb)