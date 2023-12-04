from utils import day

LINES = day(4).splitlines()

def parse_cards():
    for line in LINES:
        left, right = line.split(':')[1].split('|')
        yield len(set(left.split()) & set(right.split()))

def part1():
    print(sum((2**(n - 1)) for n in wins if n > 0))

def part2():
    sum_cards = [1] * len(wins)
    for current_card, new_cards in enumerate(wins):
        for next_card in range(current_card + 1, current_card + new_cards + 1):
            sum_cards[next_card] += sum_cards[current_card]
    print(sum(sum_cards))

wins = list(parse_cards())
part1()
part2()