import os, sys, requests, argparse

parser = argparse.ArgumentParser(
    description = 'Downloads the puzzle input from adventofcode.com, specified by Year and Day'
)
parser.add_argument('year', metavar=int, type=int, help='the year for the puzzle')
parser.add_argument('day', metavar=int, type=int, help='the day for the puzzle')
parser.add_argument('--log', default=sys.stdout, type=argparse.FileType('w'), help='log output')
args = parser.parse_args()

year, day = args.year, args.day

baseURL = lambda year, day : f'https://adventofcode.com/{year}/day/{day}/input'
baseFOLDER = lambda year, day : os.path.join(sys.path[0], f'{year}', f'day-{day}')
inputFile = 'input'

languages = {
    'python' : ['main.py']
}


url = baseURL(year, day)
folders = [baseFOLDER(year, day)]
files = []

for lang in languages.keys():
    folders.append( os.path.join(baseFOLDER(year, day), lang) )
    for file in languages[lang]:
        files.append(os.path.join( baseFOLDER(year, day), lang, file ))

for folder in folders:
    if not os.path.exists(folder):
        args.log.write(folder)
        
for file in files:
    if not os.path.exists(file):
        args.log.write(file)
        print(file)

print(folders)
print(files)