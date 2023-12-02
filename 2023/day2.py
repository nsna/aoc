import re

from utils import day

LINES = day(2).splitlines()

def part1():
    pattern = r'(\d+) (red|green|blue)'
    sum = 0
    for game, line in enumerate(LINES, start=1):
        bag = {
            'red':  12, 'green': 13, 'blue':  14
        }
        for round in line.split(';'):
            valid = True
            for num, colour in re.findall(pattern, round):
                if int(num) > bag[colour]:
                    valid = False
                    break
            if not valid:
                break
        if valid:
            sum += game
    print(sum)

def part2():
    pattern = r'(\d+) (red|green|blue)'
    sum = 0
    for line in LINES:
        bag = {
            'red':  0, 'green': 0, 'blue':  0
        }
        for round in line.split(';'):
            for num, colour in re.findall(pattern, round):
                bag[colour] = max(bag[colour], int(num))
        sum += (bag['red'] * bag['green'] * bag['blue'])
    print(sum)

part1()
part2()