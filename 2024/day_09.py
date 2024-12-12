import re
from itertools import cycle

from utils import day

RAW = "2333133121414131402"
#RAW = day(9)

def expand(disk):
    fs = {}
    is_file = cycle([True, False])
    block = 0
    file_id = 0
    for size in disk:
        if next(is_file):
            data = file_id
            file_id += 1
        else:
            data = None
        for _ in range(int(size)):
            fs[block] = data
            block += 1
    return fs

def next_free_block(fs) -> int:
    return next((key for key, value in fs.items() if value is None), -1)

def next_block_tail(fs, value) -> int:
    return next((block for block, data in reversed(fs.items()) if data == value), -1)

def next_free_segment(fs):
    start = next_free_block(fs)
    return start, get_span(fs, start)

def last_populated_block(fs):
    return next(reversed(sorted(k for k, v in fs.items() if v is not None)), -1)

def next_file(fs, prev_file):
    return next(reversed(sorted(k for k, v in fs.items() if v is not None)), -1)
    ...

def get_span(fs, start_block):
    block = start_block
    while fs[block] == fs[start_block]:
        block += 1
    return block - start_block

def get_reverse_span(fs, start_block):
    block = start_block
    while fs[block] == fs[start_block]:
        block -= 1
    return block + 1

def compact(fs):
    while True:
        last_block = last_populated_block(fs)
        first_free = next_free_block(fs)
        if last_block < first_free:
            break
        fs[first_free] = fs[last_block]
        fs[last_block] = None
    return fs

def compact_sparse(fs):
    file = fs[last_populated_block(fs)]
    print(fs)
    print()
    while file > 0:
        print(file)
        file_end = next_block_tail(fs, file)
        file_start = get_reverse_span(fs, file_end)
        file_size = (file_end - file_start) + 1
        free_start, free_size = next_free_segment(fs)

        if file_size <= free_size:
            for i in range(file_size):
                fs[free_start + i] = fs[file_start + i]
                fs[file_start + i] = None
        file -= 1
    print(fs)
    #print(file, file_start, file_size, free_start, free_size)
    #last_file_block = last_populated_block(fs)
    #file_start = get_reverse_span(fs, last_file_block)
    #file_size = (last_file_block - file_start) + 1
    #free_start, free_size = next_free_segment(fs)
    #print(file)
    #print(next_block_tail(fs, 8))


def p1():
    fs = compact(expand(RAW))
    print(sum(block * file for (block, file) in fs.items() if file is not None))

def p2():
    fs = expand(RAW)
    print(fs)
    start, size = next_free_segment(fs)
    print(start, size)
    compact_sparse(fs)


p1()
p2()
