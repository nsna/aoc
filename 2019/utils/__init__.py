import requests
import yaml
from pathlib import Path

YEAR = 2019
HERE = Path(__file__).parent
TOKEN_FILE = HERE / ".token" 
INPUTS_FILE = HERE / "inputs.yaml"

def _read_token() -> dict | None:
    if not TOKEN_FILE.is_file():
        return None
    return {"session": TOKEN_FILE.read_text().strip()}

def get_input(day: str | int) -> str:
    token = _read_token()
    url = f"https://adventofcode.com/{YEAR}/day/{day}/input"

    # create an input file if none is found
    if not INPUTS_FILE.is_file():
        INPUTS_FILE.write_text(f"info: Advent of Code {YEAR} inputs")
            
    # check if input has already been loaded
    inputs = yaml.full_load(INPUTS_FILE.read_text())
    
    if day in inputs:
        return inputs[day]
    
    # request input
    res = requests.get(url, cookies=token)
    
    if not res.ok:
        raise ValueError("request failed")
        
    # cache input
    inputs[day] = res.text.strip()
    INPUTS_FILE.write_text(yaml.dump(inputs, default_style="|"))
    return inputs[day]
    
def extract_ints(raw: str) -> map:
    """
    Extract integers from a string.
    """
    import re

    return map(int, re.findall(r'(-?\d+)', raw))