import os, sys, pyperclip

def count(string):
    return [string.count(k) for k in list(set(string))]

path = os.path.join(sys.path[0], '..', 'input')
data = open(path, 'r').read().split()
data = sum(map(count, data), [])
two, three = data.count(2), data.count(3)

answer = two * three
print("{} x {} = {}".format(two, three, answer))
pyperclip.copy(answer)