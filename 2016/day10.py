from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input10.txt'

with open(input_path, 'r') as f:
    text = f.read()

rows = text.split('\n')
print(text)
print(rows)