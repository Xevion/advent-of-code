import os, sys, pyperclip

path = os.path.join(sys.path[0], '..', 'input')
data = open(path, 'r').read()
data = map(int, data.split())
data = sum(data)

print(data)
pyperclip.copy(data)