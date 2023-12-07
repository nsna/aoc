import time
from collections import Counter
from functools import cmp_to_key
from utils import day

start_time = time.time()
LINES = day(7).splitlines()

def parse():
    for line in LINES:
        hand, bid = line.split()
        yield hand, int(bid)

def shape_values(shape):
    if shape == Counter({5: 1}):
        return 10
    elif shape == Counter({4: 1, 1: 1}):
        return 9
    elif shape == Counter({3: 1, 2: 1}):
        return 8
    elif shape == Counter({3: 1, 1: 2}):
        return 7
    elif shape == Counter({2: 2, 1: 1}):
        return 6
    elif shape == Counter({2: 1, 1: 3}):
        return 5
    else:
        return 4

def optimise_shape(counter: Counter):
    if counter == {'J': 5}:
        return Counter(counter.values())
    common = counter.most_common()
    candidate, _ = common.pop(0)
    if candidate == 'J':
        candidate, _ = common.pop(0)
    counter[candidate] += counter['J']
    del counter['J']
    return Counter(counter.values())

def cmp(a, b):
    count_a, count_b = Counter(a), Counter(b)
    shape_a, shape_b = Counter(count_a.values()), Counter(count_b.values())
    
    if MODE == 1:
        cards = P1_CARDS
    else:
        cards = P2_CARDS
        if 'J' in a:
            shape_a = optimise_shape(count_a)
        if 'J' in b:
            shape_b = optimise_shape(count_b)
        
    if shape_a == shape_b:
        for left, right in zip(a, b):
            if left == right:
                continue
            else:
                if cards.index(left) > cards.index(right):
                    return -1
                else:
                    return 1
    else:
        if shape_values(shape_a) < shape_values(shape_b):
            return -1
        else:
            return 1
    
game = dict(parse())
hands = list(game.keys())

def sort_and_sum():
    sorted_game = sorted(hands, key=cmp_to_key(cmp))
    print(sum([i * game[hand] for i, hand in enumerate(sorted_game, start = 1)]))

P1_CARDS = 'AKQJT98765432'
P2_CARDS = 'AKQT98765432J'
MODE = 1
CARDS = P1_CARDS
sort_and_sum()
MODE = 2
CARDS = P2_CARDS
sort_and_sum()
print('[Finished in {:.2f}ms]'.format(1000*(time.time() - start_time)))