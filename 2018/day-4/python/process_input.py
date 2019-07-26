import sys, os, re, datetime

# Patterns for Regex and STRPTIME function
timepattern = r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\](.+)"
strptimepattern = "%Y-%m-%d %H:%M"

def getDateTime(string):
    return datetime.datetime.strptime(re.match(timepattern, string).group(1), strptimepattern)

def process():
    newpath = os.path.join(sys.path[0], '..', 'processed_input')
    path = os.path.join(sys.path[0], '..', 'input')
    data = open(path, 'r').read().split('\n')
    return sorted(data, key=getDateTime)