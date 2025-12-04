from utils import day

RAW = day(3)
BANKS = RAW.splitlines()


def search(pool, depth):
    digits = ""
    current_position = -1
    digits_remaining = depth
    while digits_remaining:
        start = current_position + 1
        end = len(pool) - digits_remaining + 1
        digit = max(pool[start:end])
        digits += digit
        current_position = pool.index(digit, start, end)
        digits_remaining -= 1
    return int(digits)


print(p1 := sum((search(bank, 2) for bank in BANKS)))
print(p2 := sum((search(bank, 12) for bank in BANKS)))
