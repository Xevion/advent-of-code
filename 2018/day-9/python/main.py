import os
import sys
import re

from collections import deque, defaultdict

RE_PATTERN = "(\d+) players; last marble is worth (\d+) points"
PATH = os.path.join(sys.path[0], '..', 'input')
MATCH = re.match(RE_PATTERN, open(PATH, 'r').read())

PLAYERS = int(MATCH.group(1))
LAST_MARBLE = int(MATCH.group(2))

def game(players, last_marble):
    circle = deque([0])
    scores = defaultdict(int)

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    print(max(scores.values()))

game(PLAYERS, LAST_MARBLE)
game(PLAYERS, LAST_MARBLE * 100)