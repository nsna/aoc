import re
from utils import day

LINES = day(day=1, year=2023).splitlines()

def part1():
    sum = 0
    for line in LINES:
        digits = re.findall(r'(\d{1})', line)
        sum += int(digits[0] + digits[-1])
    print(sum)

def part2():
    d = {
        'one': '1',
        'two': '2',
        'three': '3', 
        'four': '4',
        'five': '5', 
        'six': '6', 
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    all_numbers = re.compile(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))')
    sum = 0
    for line in LINES:
        matches = all_numbers.findall(line)
        first = matches[0]
        last = matches[-1]
        sum += int(d.get(first, first) + d.get(last, last))
    print(sum)

part1()
part2()