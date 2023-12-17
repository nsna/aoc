from utils import day
import re
from collections import defaultdict, OrderedDict

sequence = day(15).strip()

def hash(s):
    v = 0
    for c in s:
        v += ord(c)
        v *= 17
        v %= 256
    return v

def part1():
    print(sum(hash(step) for step in sequence.split(',')))

def part2():
    hashmap = defaultdict(OrderedDict)
    for step in sequence.split(','):
        label, op, lens = re.findall(r'(\w+)(=|-)(\d*)', step)[0]
        if op == '=':
            hashmap[hash(label)][label] = int(lens)
        else:
            if label in hashmap[hash(label)]:
                del hashmap[hash(label)][label]
    print(sum((box + 1) * pos * lens 
              for box, lenses in hashmap.items() 
              for pos, lens in enumerate(lenses.values(), start=1)))

part1()
part2()