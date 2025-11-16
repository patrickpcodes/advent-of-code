from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input.txt'

with open(input_path, 'r') as f:
    text = f.read()


target = 29000000

running_total = 0
house_count = 0
house_total = 0
def get_house_total(num):
    nums = [num]
    for i in range(1, num):
        if num % i == 0:
            nums.append(i)
    return sum(nums)*10

def factors_fast(n, d=1):
    if d * d > n:
        return []

    rest = factors_fast(n, d + 1)

    if n % d == 0:
        other = n // d
        # Avoid double-counting when d == sqrt(n)
        return [d] + ([other] if other != d else []) + rest
    else:
        return rest


# while house_total < target:
#     house_count += 1
#     house_factors = factors_fast(house_count, 1)
#     house_total = sum(house_factors) * 10
#     # house_total = get_house_total(house_count)
#     print(f'Total for house {house_count} = {house_total}')
#     running_total +=  house_total

# print(running_total)
# print(house_total)
# print(house_count)


import numpy as np
goal = 29000000
BIG_NUM = 1000000
houses = np.zeros(BIG_NUM)
for elf in range(1, BIG_NUM):
    houses[elf::elf] += 10 * elf
print(np.nonzero(houses >= goal))
print(np.nonzero(houses >= goal)[0][0])

houses = np.zeros(BIG_NUM)
for elf in range(1, BIG_NUM):
    houses[elf:(elf+1)*50:elf] += 11 * elf
print(np.nonzero(houses >= goal))
print(np.nonzero(houses >= goal)[0][0])

