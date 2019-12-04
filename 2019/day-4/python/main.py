import os
import sys
import re

PATH = os.path.join(sys.path[0], '..', 'input')
DATA = list(map(int, open(PATH, 'r').read().split('-')))

def criteria(n):
    digits = list(map(int, list(str(n))))
    repeats = False
    prev = digits[0]

    for digit in digits[1:]:
        if prev == digit:
            repeats = True
        if prev > digit:
            return False
        prev = digit
    return repeats

def rerepeats(n):
    return 2 in [len(m[0]) for m in re.finditer(r'(\d)\1+', str(n))]

passwords = [x for x in range(DATA[0], DATA[1]) if criteria(x)]
print(len(passwords))
passwords = [x for x in passwords if rerepeats(x)]
print(len(passwords))