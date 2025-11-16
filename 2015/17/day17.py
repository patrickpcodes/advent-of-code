from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input.txt'

with open(input_path, 'r') as f:
    text = f.read()

rows = text.split("\n")
data = sorted([int(r) for r in rows])
data.reverse()
print(data)

total = 150
count = 0

def get_num_combinations(target, nums):
    count = 0
    for i in range(len(nums)):
        item = nums[i]
        if item == target:
            count += 1
        elif item > target:
            continue
        else:
            count += get_num_combinations(target-item, nums[i+1:])
    return count

print(get_num_combinations(total, data))

import itertools
num = 0
min_count = 30
for i in range(len(data)): # range(0,20)
    for subset in itertools.combinations(data, i):
        if sum(subset) == 150:
            num += 1
            if len(subset) < min_count: min_count = len(subset)
print(num)
print(f"Min number = {min_count}")
count = 0
for i in range(len(data)): # range(0,20)
    for subset in itertools.combinations(data, i):
        if sum(subset) == 150 and len(subset) == min_count:
            count += 1
            # if len(subset) < min_count: min_count = len(subset)
print(f"Count with min : {count}")
