from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input_1.txt'

with open(input_path, 'r') as f:
    text = f.read()

curr_a = (0, 0)
curr_b = (0, 0)
dic = {}
dic[(0,0)] = 2

def move_location(item, current):
    if item == "^":
        return (current[0], current[1]+1)
    if item == ">":
        return (current[0]+1, current[1])
    if item == "v":
        return (current[0], current[1]-1)
    if item == "<":
        return (current[0]-1, current[1])


for i, item in enumerate(text):
    if i % 2 == 0:
        curr_a = move_location(item, curr_a)
        if curr_a in dic:
            dic[curr_a] += 1
        else:
            dic[curr_a] = 1
    else:
        curr_b = move_location(item, curr_b)
        if curr_b in dic:
            dic[curr_b] += 1
        else:
            dic[curr_b] = 1


print(len(dic.keys()))