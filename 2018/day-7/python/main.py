import os, sys, time, re, collections, string

# Input file reading
path = os.path.join(sys.path[0], '..', 'input')
data = open(path, 'r').read().split('\n')
# data = """Step C must be finished before step A can begin.
# Step C must be finished before step F can begin.
# Step A must be finished before step B can begin.
# Step A must be finished before step D can begin.
# Step B must be finished before step E can begin.
# Step D must be finished before step E can begin.
# Step F must be finished before step E can begin.""".split('\n')

# Constants and Setup
regexpattern = r"Step (\w) must be finished before step (\w) can begin."
def parse(item):match = re.match(regexpattern, item);return [match[1], match[2]]
data = list(map(parse, data))
reqs = collections.defaultdict(list)
for before, after in data:
        reqs[before]
        reqs[after].append(before)
data = list(map(list, reqs.items()))

COL_JOINER, COL_SECOND, COL_WORKER, COL_RESULT = '  ', 10, 8   , 26

class Factory(object):
    def __init__(self, workers, data):
        self.worker_count, self.data = workers, data
        self.workers = [0 for _ in range(self.worker_count)]
        self.working_jobs = [''] * self.worker_count
        self.result = ""
        self.duration = 0
        self._table = []
        header = [' Second'.center(COL_SECOND)]
        header.extend([f'Worker {i+1}'.center(COL_WORKER) for i in range(self.worker_count)])
        header.append('Result'.ljust(COL_RESULT))
        self._table.append(COL_JOINER.join(header))
        self.loop()
    
    # returns the duration score value for a given step (char)
    def get_duration(self, char):
        return 60 + ( string.ascii_uppercase.find(char.upper()) + 1 )

    @property
    def active(self):
        return len(self.data) > 0 or any([worker > 0 for worker in self.workers])

    # Mainloop which is the driver code.
    def loop(self):
        # self.report([self.duration, self.result, self.working_jobs])
        self.tick()
        while self.active:
            self.report()
            self.duration += 1
            self.tick()
        self.report()

    @property
    def available_jobs(self, all=False):
        possible = []
        for i in range(len(self.data)):
            # if no requirements left, make it a possible
            if len(self.data[i][1]) == 0:
                possibility = (i, self.data[i][0])
                if possibility[1] not in self.working_jobs:
                    possible.append( possibility )
        # sort alphabetical
        possible.sort(key=lambda item : item[1])
        # [(INDEX, CHARACTER), (INDEX2, CHARACTER2)]
        return possible

    # Removes char from all item values (does not remove key itself)
    def cleanse(self, char):
        def clean(item):
            return item[0], [i for i in item[1] if i != char]
        self.data = list(map(clean, self.data))

    # dispatches a job and adds a duration to the worker
    def dispatch(self, id):
        choices = self.available_jobs
        if len(choices) == 0:
            return
        else:
            choice = choices.pop(0)
            self.data.pop(choice[0])
            self.workers[id] = self.get_duration(choice[1])
            self.working_jobs[id] = str(choice[1])

    def report(self):
        second, result, jobs = list([self.duration, self.result, self.working_jobs])
        row = [str(second).center(COL_SECOND)]
        for job in jobs:
            row.append(('.' if job == '' else job).center(COL_WORKER))
        row.append(result.ljust(COL_RESULT))
        self._table.append(COL_JOINER.join(row))

    @property
    def table(self):
        return '\n'.join(self._table)

    # Ticks a single second. Dispatches jobs to workers
    def tick(self):
        for i in range(len(self.workers)):
            if self.workers[i] > 0:
                self.workers[i] -= 1
                # Was working, is no longer.
                if self.workers[i] == 0:
                    self.result += self.working_jobs[i]
                    self.cleanse(self.working_jobs[i])
                    # I have no idea why, but settings self.working_jobs[i] = '' DOES NOT WORK.
                    self.working_jobs = ['' if index == i else item for index, item in enumerate(self.working_jobs)]
            if self.workers[i] == 0:
                self.dispatch(i)

f = Factory(5, data)
print(f.table)
print(f.result, f.duration)