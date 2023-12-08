import time
from utils import day

start_time = time.time()
LINES = day(7).splitlines()

def score_hand(hand):
    # map the number of times a character appears
    # sorting in reverse order makes the higher ranked hands position last
    return sorted(map(hand.count, hand), reverse=True)

def parse(face):
    for line in LINES:
        hand, bid = line.split()
        # translating the face cards into ABCDE allows
        # python sort to work on the character ordinals
        # which means automatic high card sorting
        hand = hand.translate(str.maketrans('TJQKA', face))
        #print(max(score_hand(hand)), score_hand(hand), hand)
        # part 2 find the highest score possible when substituting J (0)
        # part 1 will be unaffected since 0 will not exist in the hand
        best = max(score_hand(hand.replace('0', card)) for card in hand)
        yield best, hand, int(bid)

def part1():
    print(sum(rank * bid for rank, (_, _, bid) in enumerate(sorted(parse('ABCDE')), start=1)))

def part2():
    # J matches up with B but we want it scoring the lowest this time
    # so replace B with a char lower than '1' -> '0'
    print(sum(rank * bid for rank, (_, _, bid) in enumerate(sorted(parse('A0CDE')), start=1)))

part1()
part2()
print('[Finished in {:.2f}ms]'.format(1000*(time.time() - start_time)))