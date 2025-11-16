from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input.txt'

with open(input_path, 'r') as f:
    text = f.read()

dest_row = 2947
dest_col = 3029


def get_triangle_num(n):
    return n * (n + 1) // 2

def get_id_num(row, col):
    r = row
    c = col
    dist = col - 1
    if row != 1:
        r = row + dist

    first_t_num = get_triangle_num(r-1)
    # print(first_t_num)
    val = first_t_num + 1
    return val + dist



test_data = []
test_data.append((2, 2, 5))
test_data.append((4,2, 12))
test_data.append((2,5, 20))
test_data.append((dest_row, dest_col))

for t in test_data:
    print(get_id_num(t[0], t[1]))

id_target = get_id_num(2947, 3029)

starting_code = 20151125
def get_next_code(code):
    c = code * 252533
    return c % 33554393

next_code = starting_code
for i in range(id_target-1):
    next_code = get_next_code(next_code)

print(next_code)