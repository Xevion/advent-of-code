import os, sys, time, progressbar, string

path = os.path.join(sys.path[0], '..', 'input')
data = open(path, 'r').read()
# data = data[:10000]
data = 'dabAcCaCBAcCcaDA'

def react(string):
    look = True
    while look:
        look = False
        for i in range(len(string)-1):
            if string[i].lower() == string[i + 1].lower() and string[i] != string[i + 1]:
                string = string[:i] + string[i+2:]
                look = True
                break
    return string

# t1 = time.time()
# data = react(data) #11476
# t2 = time.time()
# print('Part 1 Solution: {}'.format(len(data)))
# print('Solved in {}s\n'.format(round(t2 - t1, 3)))

t1 = time.time()
lengths = {}
charset = ''.join(list(set(data)))
for char in progressbar.progressbar(list(charset)):
    table = str.maketrans({char : None, char.lower() : None})
    lengths[char] = len(react(data.translate(table)))
char, length = min(lengths.items(), key=lambda item : item[1])
t2 = time.time()
 
print('\nPart 2 Solution: Removing polymer {}{} had the most effect at length {}.'.format(char, char.lower(), length))
print('Solved in {}s\n'.format(round(t2 - t1, 3)))