import os, sys, pyperclip

def count(string):
    return list(set([string.count(k) for k in list(set(string))]))

path = os.path.join(sys.path[0], '..', 'input')
data = open(path, 'r').read().split('\n')
sums = sum(map(count, data), [])
two, three = sums.count(2), sums.count(3)

answer = two * three
print("{} x {} = {}".format(two, three, answer))
pyperclip.copy(answer)

try:
    for id1 in data:
        for id2 in data:
            diff = [i for i in range(len(id1)) if id1[i] != id2[i]]
            if len(diff) == 1:
                e = [id1[i] for i in range(len(id1)) if i not in diff]
                print(''.join(e))
                raise Exception()
except:
    pass