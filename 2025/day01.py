from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input01.txt'

with open(input_path, 'r') as f:
    text = f.read()

rows = text.split('\n')
# print(rows)


def get_next_position(start, movement):
    d, num = movement[0], int(movement[1:])
    num = num % 100
    times = 0
    if d == "L":
        v =  start - num
        if start - num >0:
            return (v, times)
        elif start - num == 0:
            return (v, times + 1)
        else:
            return (start - num + 100, times )
    else:
        v = start + num
        if start + num == 100 or start + num == 0:
            return (0, times + 1)
        elif start + num < 100:
            return (v, times)
        else:
            return (start + num - 100, times )

def get_next_position_times_passing_0(start, movement):
    d, num = movement[0], int(movement[1:])
    times = 0
    while num >=100:
        num -= 100
        times += 1
    if d == "L":
        v =  start - num
        if start - num >0:
            return (v, times)
        elif start - num == 0:
            return (v, times + 1)
        else:
            if start == 0:
                times -= 1
            return (start - num + 100, times + 1)
    else:
        v = start + num
        if start + num == 100 or start + num == 0:
            return (0, times + 1)
        elif start + num < 100:
            return (v, times)
        else:
            if start == 0:
                times -= 1
            return (start + num - 100, times + 1 )
    # return (v , times)


count = 0
current_pos = 50
for r in rows:
    current_pos, times = get_next_position(current_pos, r)
    # print(f"The dial is rotated {r} to point at {current_pos}.")
    count += times
    # if current_pos == 0:
    #     count += 1

print(f"Number of times at 0 is {count}")

current_pos = 50
count = 0
for r in rows:
    current_pos, times = get_next_position_times_passing_0(current_pos, r)
    print(f"The dial is rotated {r} to point at {current_pos}. during this rotation, it points at 0 {times} times")
    count += times
    if current_pos == 0:
        count += 0

print(f"Number of times at 0 is {count}")
