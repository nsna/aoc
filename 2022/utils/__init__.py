import requests
import yaml
import os
from pathlib import Path

YEAR = 2022
HERE = Path(__file__).parent
TOKEN_FILE = HERE / ".token" 
INPUTS_FILE = HERE / "inputs.yaml"

def _read_token() -> dict | None:
    if not TOKEN_FILE.is_file():
        return None
    return {"session": TOKEN_FILE.read_text().strip()}

def day(day: str | int) -> str:
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