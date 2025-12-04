from utils import day

RAW = day(3)


def search(pool, depth):
    digits = ""
    current_position = -1
    digits_remaining = depth
    while digits_remaining:
        # determine window
        start = current_position + 1
        end = len(pool) - digits_remaining + 1
        # find max
        digit = max(pool[start:end])
        digits += digit
        # update index and remaining digits
        current_position = pool.index(digit, start, end)
        digits_remaining -= 1
    return int(digits)


print(p1 := sum((search(bank, 2) for bank in RAW.splitlines())))
print(p2 := sum((search(bank, 12) for bank in RAW.splitlines())))
