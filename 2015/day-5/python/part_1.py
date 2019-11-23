import os
import sys
import re

PATH = os.path.join(sys.path[0], '..', 'input')
DATA = open(PATH, 'r').read().split('\n')
PATTERN = r'(\w)\1'

def req1(string):
    count = 0
    for vowel in list('aeiou'):
        count += string.count(vowel)
        if count >= 3:
            return  True
    return False

def req2(string):
    return bool(re.search(PATTERN, string))

def req3(string):
    for sub in ['ab', 'cd', 'pq', 'xy']:
        if sub in string:
            return False
    return True

def reqAll(string):
    return req3(string) and req1(string) and req2(string)

i = 0
for line in DATA:
    i += 1 if reqAll(line) else 0 
print(i)