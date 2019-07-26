import time, re, datetime, pprint, process_input

# Returns processed input, simple script for creating a chronologically ordered input file.
data = process_input.process()

# Comment this out to use real puzzle data
# import sys, os
# path = os.path.join(sys.path[0], '..', 'processed_input')
# data = open(path, 'r').read().split('\n')

# Pattern Constants & pprint
pprint = pprint.PrettyPrinter(width=1000).pprint
timepattern = r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\](.+)"
guard_id_pattern = r"Guard #(\d+) begins shift"
strptimepattern = "%Y-%m-%d %H:%M"

class GuardData:
    def __init__(self, quiet=False):
        self.quiet = quiet
        self.guards = {}
    
    # Grabs the guard with the best singular minute
    def best_minute(self):
        # Finds the guard based on the guard's most slept minute
        guard =  max(self.guards.items(), key=lambda item : max(enumerate(item[1]['minutes']), key=lambda minute : minute[1]))
        # Return the guard selected's best minute and the minute count and the id of the guard.
        return guard[0], max(enumerate(guard[1]['minutes']), key=lambda item : item[1])

    # Returns the guard item with the highest total
    def best_total(self):
        best = max(self.guards.items(), key=lambda item : item[1]['total'])
        return best[0], best[1]['total']

    # Returns the minute the guard selected was asleep the most, along with how much
    def guard_best_minute(self, id):
        return max(enumerate(self.guards[id]['minutes']), key=lambda item : item[1])

    # Simply ensures the guard exists.
    # Otherwise, it will initalize a guard with the id.
    def ensure_exists(self, id):
        if id in self.guards.keys():
            return
        else:
            self.guards[id] = {
                'total' : 0,
                'minutes' : [0 for i in range(60)]
            }

    # ID, Time Point 1, Time Point 2, Type
    def add_sleep_time(self, id, t1, t2):
        self.ensure_exists(id)
        minutes = (t2 - t1) // datetime.timedelta(minutes=1)
        print(f'Guard #{id} slept for {minutes} minutes from \'{t1}\' to \'{t2}\'')
        # print('id-{} : {}mins : {} --> {}'.format(id, minutes, t1, t2))
        for minute in range(minutes):
            self.guards[id]['minutes'][( t1.minute + (minute % 60) ) % 60] += 1
        self.guards[id]['total'] += minutes

guard_data = GuardData(quiet=True)
current_guard = None
current_action = None
last_timechange = None

for line in data:
    match = re.match(timepattern, line)
    time = datetime.datetime.strptime(match.group(1), strptimepattern)
    action = match.group(2).strip()
    
    # Detect whether the most recent change is a guard change
    is_guard_change = re.match(guard_id_pattern, action)
    if is_guard_change:
        current_guard = int(is_guard_change.group(1))
        last_timechange = time
        current_action = None
    # Ignore if status has not changed
    elif action != current_action:
        if action == 'falls asleep':
            pass
        elif action == 'wakes up' and current_action == 'falls asleep':
            guard_data.add_sleep_time(current_guard, last_timechange, time)
        else:
            print('Unknown Action : \'{}\''.format(action))
        current_action = action
        last_timechange = time


id, total = guard_data.best_total()
minute, minute_count = guard_data.guard_best_minute(guard_data.best_total()[0])
print(f'\nGuard {id} slept the most for a total of {total} minutes.')
print(f'Guard {id} slept the most during minute {minute} a total of {minute_count} times.')
p1 = id * minute

id, (minute, minute_count) = guard_data.best_minute()
print(f'Guard {id} spent minute {minute} the most @ {minute_count} times.')
p2 = id * minute

print(f'\nPart 1 solution: {p1}\nPart 2 solution: {p2}')