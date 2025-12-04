
from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input03.txt'

with open(input_path, 'r') as f:
    text = f.read()


#text = "987654321111111\n811111111111119\n234234234234278\n818181911112111"


rows = text.split("\n")

def get_max_number_in_sub(s, length):
    max = 0
    max_index = 0
    range_len = len(s) -(length -1)
    for i in range(range_len):
        if int(s[i]) > max:
            max = int(s[i])
            max_index = i
        if max == 9:
            break
    if length == 1:
        return str(max)
    return str(max) + get_max_number_in_sub(s[max_index+1:], length -1 )


sum = 0
for r in rows:
    d = get_max_number_in_sub(r, 2)
    sum += int(d)
print(f"Sum for 2 = {sum}")

sum = 0
for r in rows:
    d = get_max_number_in_sub(r, 12)
    sum += int(d)
print(f"Sum for 12 = {sum}")