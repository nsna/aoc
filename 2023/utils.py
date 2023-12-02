import os
import re
from pathlib import Path

import requests

def day(day: str | int, year: int= 2023) -> str:
    """
    Retrieve an input for advent of code day
    """
    token_file = Path("./.token")
    if not token_file.exists():
        raise ValueError("session token not found")
    token = {"session": token_file.read_text().strip()}

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    
    # https://www.reddit.com/r/adventofcode/comments/z9dhtd/please_include_your_contact_info_in_the_useragent/
    discord = os.getenv('DISCORD')
    if discord is None:
        raise ValueError("set DISCORD environment variable for request contact info")
    
    headers = {
        'User-Agent': f"https://github.com/nsna/aoc | discord:{discord}"
    }
    
    inputs_folder = Path("./inputs")
    if not inputs_folder.exists():
        inputs_folder.mkdir()

    input_file = inputs_folder / f"{day}.txt"
    if input_file.is_file():
        return input_file.read_text()
   
    # request input
    res = requests.get(url, cookies=token, headers=headers)

    if not res.ok:
        print(res.content)
        raise ValueError("request failed")
        
    # cache input + remove any trailing newlines
    raw_input = res.text.rstrip()
    input_file.write_text(raw_input)
    return raw_input

def ints(raw: str) -> map:
    """
    Extract integers from a string.
    """
    return map(int, re.findall(r'(-?\d+)', raw))
    
def pos_ints(raw: str) -> map:
    """
    Extract only positives integers from a string
    """
    return map(int, re.findall(r'(\d+)', raw))
