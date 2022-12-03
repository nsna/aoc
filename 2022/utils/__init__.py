import requests
import yaml
import os
import time
from pathlib import Path

YEAR = 2022
HERE = Path(__file__).parent
TOKEN_FILE = HERE / ".token" 
INPUTS_FILE = HERE / "inputs.yaml"

class Benchmark:
    def __init__(self):
        self.start = time.time()
        self.end = self.start
    
    def update(self):
        self.end = time.time()
        
    def __str__(self):
        return f"{(self.end - self.start) * 1000:.2f}ms"
            
def _read_token() -> dict | None:
    """
    Read local token file used for retrieving inputs in day function
    """
    if not TOKEN_FILE.is_file():
        return None
    return {"session": TOKEN_FILE.read_text().strip()}

def day(day: str | int) -> str:
    """
    Retrieve an input for advent of code day
    Year is a constant
    """
    token = _read_token()
    if token is None:
        raise ValueError("token not found")
        
    url = f"https://adventofcode.com/{YEAR}/day/{day}/input"
    
    #https://www.reddit.com/r/adventofcode/comments/z9dhtd/please_include_your_contact_info_in_the_useragent/
    discord = os.getenv('DISCORD')
    if discord is None:
        raise ValueError("set discord environment variable for request contact info")
    
    headers = {
        'User-Agent': f"https://github.com/nsna/aoc | discord:{discord}"
    }
    
    # create an input file if none is found
    if not INPUTS_FILE.is_file():
        INPUTS_FILE.write_text(f"info: Advent of Code {YEAR} inputs")
            
    # check if input has already been loaded
    inputs = yaml.full_load(INPUTS_FILE.read_text())
    
    if day in inputs:
        return inputs[day]
    
    # request input
    res = requests.get(url, cookies=token, headers=headers)
    
    if not res.ok:
        raise ValueError("request failed")
        
    # cache input
    inputs[day] = res.text.strip()
    INPUTS_FILE.write_text(yaml.dump(inputs, default_style="|"))
    return inputs[day]
    
def ints(raw: str) -> map:
    """
    Extract integers from a string.
    """
    import re

    return map(int, re.findall(r'(-?\d+)', raw))
    
def directions(raw: str) -> list:
    """
    Extract 2D directions from input, i.e. U201
    """
    import re
    
    pattern = re.compile('((\w)(\d+))')
    values = map(pattern.findall, raw)
    return [(value[1], int(value[2])) for value in values]
  
def rshift(iterable, n):
    """
    Shift all values in iterable to the right by n places
    """
    from itertools import islice, cycle

    l = len(iterable)
    return islice(cycle(iterable), l - (n % l), 2 * l - (n % l))

def lshift(iterable, n):
    """
    Shift all values in iterable to the left by n places
    """
    from itertools import islice, cycle

    l = len(iterable)
    return islice(cycle(iterable), n, n + l)
    
def nth(iterable, n):
    """
    Return nth item of iterable
    """
    from itertools import islice

    return next(islice(iterable, n, None))
    
def delta4(coord) -> tuple: 
    """
    Four neighbouring cells (without diagonals).
    """
    x, y = coord
    return ((x+1, y), (x-1, y), (x, y+1), (x, y-1))

def delta8(coord) -> tuple: 
    """
    Eight neighbouring cells (with diagonals).
    """
    x, y = coord 
    return ((x+1, y), (x-1, y), (x, y+1), (x, y-1),
            (x+1, y+1), (x-1, y-1), (x+1, y-1), (x-1, y+1))
            
# Shorthand functions to get X and Y coordinates out of
# a tuple or list 
def X(coord): return coord[0]
def Y(coord): return coord[1]

def manhattan_distance(a, b=(0,0)) -> int:
    """
    Manhattan distance between point a and b (default origin)
    """
    return abs(X(a) - X(b)) + abs(Y(a) - Y(b))