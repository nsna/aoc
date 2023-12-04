from utils import day
import re
import time
LINES = day(4).splitlines()

start_time = time.time()

def parse_cards():
    wins = {}
    for i, line in enumerate(LINES, start = 1):
        numbers = re.findall(r'(\d+)', line)
        wins[i] = len(set(numbers[1:11]) & set(numbers[11:]))
    return wins

def part1():
    print(sum((2**(n - 1)) for n in wins.values() if n > 0))

def part2():
    sum_cards = dict(list(enumerate([1] * len(wins), start = 1)))
    for current_card, new_cards in wins.items():
        for next_card in range(current_card + 1, current_card + new_cards + 1):
            sum_cards[next_card] += sum_cards[current_card]
    print(sum(sum_cards.values()))

wins = parse_cards()
part1()
part2()
print ('[Finished in {:.2f}ms]'.format(1000*(time.time() - start_time)))