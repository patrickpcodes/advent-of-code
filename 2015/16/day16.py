from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input.txt'

with open(input_path, 'r') as f:
    text = f.read()

input_path = script_dir / 'data.txt'
with open(input_path, 'r') as f:
    d = f.read()

data = {}
for item in d.split("\n"):
    a, b = item.split(": ")
    data[a] = int(b)
print(data)

text = text.replace("Sue ", " ")



sues = {}
rows = text.split("\n")
for row in rows:
    print(row)
    a, d = row.split(":", 1)
    a, d = int(a), d.strip()
    items = d.split(",")
    sues[a] = {}
    for item in items:
        k, v = item.split(":")
        sues[a][k.strip()] = int(v)
    print(sues)

for s in sues.keys():
    found = True
    for i in sues[s].keys():
        if sues[s][i] != data[i]:
            found = False
    if found:
        print(f"Found sue {s}")

for s in sues.keys():
    found = True
    for i in sues[s].keys():
        if i == "cats" or i == "trees":
            if sues[s][i] <= data[i]:
                found = False
        elif i == "pomeranians" or i == "goldfish":
            if sues[s][i] >= data[i]:
                found = False
        elif sues[s][i] != data[i]:
            found = False
    if found:
        print(f"Found sue {s}")