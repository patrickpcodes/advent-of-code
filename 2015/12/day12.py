from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input.txt'



import json

with open(input_path, 'r') as f:
    abacus = json.load(f)

print(abacus)

def sum_numbers(item, ignore_red=False):
    if isinstance(item, list):
        return sum([sum_numbers(i, ignore_red) for i in item])
    if isinstance(item, dict):
        if "red" in item.keys() or "red" in item.values() and ignore_red:
            return 0
        return sum([sum_numbers(i, ignore_red) for i in item.values()])
    if isinstance(item, str):
        return 0
    if isinstance(item, int):
        return item

print(sum_numbers(abacus))
print(sum_numbers(abacus, True))