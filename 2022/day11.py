from utils import day, ints
from functools import partial
from collections import deque
from heapq import nlargest
from math import prod
from operator import add, mul, sub, attrgetter
# import operator

#RAW = day(11)

RAW = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

# RAW = day(11)

class Monkey:
    def __init__(self, n, items, func, test):
        self.n = n
        self.items = deque(items)
        self.func = func
        self.test = test
        self.monkey_true = None
        self.monkey_false = None
        self.inspected = 0
    
    def inspect(self):
        while self.items:
            item = self.items.popleft()
            self.inspected += 1
            worry = self.func(item)
            # worry //= 3
            if worry % self.test == 0:
                self.monkey_true.items.append(worry)
            else:
                self.monkey_false.items.append(worry)
    
    def __lt__(self, other):
        return self.inspected < other.inspected
    
    def __str__(self):
        return f"n: {self.n}, items: {self.items}"

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
monkeys = parse()

for _ in range(10_000):
    for monkey in monkeys:
        monkey.inspect()
    
print(prod(map(attrgetter('inspected'), nlargest(2, monkeys))))
# for monkey in monkeys:
#     print(monkey.n, monkey.inspected)
    
# print(monkeys[0])
# monkeys[0].inspect()
# print(monkeys[3])
# print(monkeys[0])
# print(monkeys[0].monkey_true)
# print(monkeys[0].monkey_false)