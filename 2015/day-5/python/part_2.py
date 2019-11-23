import os
import sys
import re

PATH = os.path.join(sys.path[0], '..', 'input')
DATA = open(PATH, 'r').read().split('\n')
PATTERN_1 = r'.*(\w\w).*\1.*'
PATTERN_2 = r'(\w)\w\1'

def req1(string):
    return bool(re.match(PATTERN_1, string))

def req2(string):
    return bool(re.search(PATTERN_2, string))

def reqAll(string):
    return req1(string) and req2(string)

i = 0
for line in DATA:
    i += 1 if reqAll(line) else 0
print(i)