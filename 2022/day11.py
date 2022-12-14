from utils import day, ints
from functools import partial
from collections import deque
from heapq import nlargest
from math import prod
from operator import add, mul, sub, attrgetter

RAW = day(11)

class Monkey:
    def __init__(self, n, items, func, test):
        self.n = n
        self.items = deque(items)
        self.func = func
        self.test = test
        self.monkey_true = None
        self.monkey_false = None
        self.inspected = 0
    
    def inspect(self, part2=None):
        while self.items:
            item = self.items.popleft()
            self.inspected += 1
            worry = self.func(item)
            if part2:
                worry %= part2
            else:
                worry //= 3
            if worry % self.test == 0:
                self.monkey_true.items.append(worry)
            else:
                self.monkey_false.items.append(worry)
    
    def __lt__(self, other):
        return self.inspected < other.inspected
    
def parse():
    monkeys = []
    neighbours = []
    
    # parse input
    for monkey in RAW.split('\n\n'):
        notes = monkey.splitlines()
        n = int(notes[0][-2:-1])
        items = list(ints(notes[1]))
        op, v = notes[2].split()[-2:]
        if v == 'old':
            func = partial(squared)
        else:
            func = partial(ops[op], int(v))
        neighbours.append(list(ints(''.join(notes[4:]))))
        test = int(notes[3].split()[-1])
        monkeys.append(Monkey(n, items, func, test))
        
    # link monkeys
    for i, neighbour in enumerate(neighbours):
        monkeys[i].monkey_true = monkeys[neighbour[0]]
        monkeys[i].monkey_false = monkeys[neighbour[1]]
    return monkeys

squared = lambda a: a**2
ops = {'*': mul, '+': add, '-': sub}
part1 = parse()

# part1
for _ in range(20):
    for monkey in part1:
        monkey.inspect()
    
print(prod(map(attrgetter('inspected'), nlargest(2, part1))))

# part2
part2 = parse()
mod = prod(map(attrgetter('test'), part2))
for _ in range(10_000):
    for monkey in part2:
        monkey.inspect(mod)
        
print(prod(map(attrgetter('inspected'), nlargest(2, part2))))
