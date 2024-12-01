import os
from pathlib import Path
import time
import requests

from dotenv import load_dotenv

def day(day: str | int, year: int= 2024) -> str:
    """
    Retrieve an input for advent of code day
    """
    load_dotenv()
    token = os.getenv('TOKEN')
    if token is None:
        raise ValueError("TOKEN env variable not set for session token")
    cookies = {"session": token}

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
    res = requests.get(url, cookies=cookies, headers=headers)

    if not res.ok:
        print(res.content)
        raise ValueError("request failed")
        
    # cache input + remove any trailing newlines
    raw_input = res.text.rstrip()
    input_file.write_text(raw_input)
    return raw_input

def measure_time(func):
    def wrapper():
        start_time = time.time()
        func()
        print('[Finished in {:.2f}ms]'.format(1000*(time.time() - start_time)))
    return wrapper
    