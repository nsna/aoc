import os
from pathlib import Path

YEAR = 2023
HERE = Path(__file__).parent

def day(day: str | int) -> str:
    """
    Retrieve an input for advent of code day

    Year is a constant
    """
    import requests

    TOKEN_FILE = HERE / ".token"
    if not TOKEN_FILE.exists():
        raise ValueError("session token not found")
    token = {"session": TOKEN_FILE.read_text().strip()}

    url = f"https://adventofcode.com/{YEAR}/day/{day}/input"
    
    # https://www.reddit.com/r/adventofcode/comments/z9dhtd/please_include_your_contact_info_in_the_useragent/
    discord = os.getenv('DISCORD')
    if discord is None:
        raise ValueError("set DISCORD environment variable for request contact info")
    
    headers = {
        'User-Agent': f"https://github.com/nsna/aoc | discord:{discord}"
    }
    
    INPUTS_FOLDER = HERE / "inputs"
    if not INPUTS_FOLDER.exists():
        INPUTS_FOLDER.mkdir()

    INPUTS_FILE = INPUTS_FOLDER / f"{day}.txt"
    if INPUTS_FILE.is_file():
        return INPUTS_FILE.read_text()
   
    # request input
    res = requests.get(url, cookies=token, headers=headers)

    if not res.ok:
        raise ValueError("request failed")
        
    # cache input + remove any trailing newlines
    RAW = res.text.rstrip()
    INPUTS_FILE.write_text(RAW)
    return RAW

def ints(raw: str) -> map:
    """
    Extract integers from a string.
    """
    import re

    return map(int, re.findall(r'(-?\d+)', raw))
    
def pos_ints(raw: str) -> map:
    """
    Extract only positives integers from a string
    """
    import re
    
    return map(int, re.findall(r'(\d+)', raw))
