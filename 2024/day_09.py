import re
from itertools import cycle
from collections import defaultdict

from utils import day

RAW = "2333133121414131402"
RAW = day(9)

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

def all_free_segments(fs):
    free_blocks = defaultdict(int)
    seq = None
    for key, value in fs.items():
        if value is None:
            if seq is None:
                seq = key
            free_blocks[seq] += 1
        else:
            seq = None
    return free_blocks

def next_free_block(fs) -> int:
    return next((key for key, value in fs.items() if value is None), -1)

def next_block_tail(fs, value) -> int:
    return next((block for block, data in reversed(fs.items()) if data == value), -1)

def next_free_segment(fs):
    start = next_free_block(fs)
    return start, get_span(fs, start)

def last_populated_block(fs):
    return next(reversed(sorted(k for k, v in fs.items() if v is not None)), -1)

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

def defrag(fs):
    while True:
        last_block = last_populated_block(fs)
        first_free = next_free_block(fs)
        if last_block < first_free:
            break
        fs[first_free] = fs[last_block]
        fs[last_block] = None
    return fs

def to_str(fs):
    for k, v in fs.items():
        if v is not None:
            print(v, end="")
        else:
            print('.', end="")
    print()

def defrag2(fs):
    file = fs[last_populated_block(fs)]
    while file > 0:
        file_end = next_block_tail(fs, file)
        file_start = get_reverse_span(fs, file_end)
        file_size = (file_end - file_start) + 1
        free_segments = all_free_segments(fs)
        free_start = next(iter(start for (start, size) in free_segments.items() if file_size <= size), None)
        if (free_start is not None and free_start < file_start):
            for i in range(file_size):
                fs[free_start + i] = fs[file_start + i]
                fs[file_start + i] = None
        file -= 1
    return fs

def p1():
    fs = defrag(expand(RAW))
    print(sum(block * file for (block, file) in fs.items() if file is not None))

def p2():
    fs = defrag2(expand(RAW))
    print(sum(block * file for (block, file) in fs.items() if file is not None))

p1()
p2()
