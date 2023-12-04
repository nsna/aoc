from utils import day
import re
from functools import lru_cache
from collections import Counter, deque
LINES = day(4).splitlines()

@lru_cache
def calculate_card(n):
    winning, hand = LINES[n - 1].split('|')
    winning_nums = set(re.findall(r'(\d+)', winning.split(':')[1]))
    hand_nums = set(re.findall(r'(\d+)', hand))
    return len(winning_nums & hand_nums)

def part1():
    sum = 0
    for n in range(len(LINES) + 1):
        wins = calculate_card(n)
        if wins:
            sum += 2**(wins - 1)
    print(sum)

def part2():
    cards = Counter()
    queue = deque(range(1, len(LINES) + 1))
    while queue:
        card = queue.popleft()
        cards[card] += 1
        new_cards = calculate_card(card)
        if new_cards:
            queue.extend(range(card + 1, card + new_cards + 1))

    print(sum(cards.values()))

part1()
part2()