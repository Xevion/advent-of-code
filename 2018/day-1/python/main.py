import os, sys, pyperclip, itertools, time

t1 = time.time()
path = os.path.join(sys.path[0], '..', 'input')
data = open(path, 'r').read()
data = list(map(int, data.split('\n')))
# data = [+7, +7, -2, -7, -4]
datacycle = itertools.cycle(data)
final = sum(data) # day 1 solution

curfreq = 0
i = 0
prevfreq = set()
searching = True
while searching:
    i += 1
    curfreq += next(datacycle)
    if curfreq in prevfreq:
        searching = False
        break
    prevfreq.add(curfreq)
t2 = time.time()

print("Calculation completed in {}ms".format( round((t2 - t1) * 1000, 2) ))
print("Final Frequency: {}".format(final))
print("Frequency {} repeated after {} iterations.".format(curfreq, i))