from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input08.txt'

with open(input_path, 'r') as f:
    text = f.read()

rows = text.split('\n')

grid = [["." for _ in range(50)] for _ in range(6)]
print(grid)

print(rows)

def create_rect(grid, x, y):
    for j in range(y):
        for i in range(x):
            grid[j][i] = "#"
    return grid

def rotate_column(grid, col, times):
    col_length = len(grid)
    new_col = ['.'] * col_length
    for i in range(col_length):
        val = grid[i][col]
        new_col[(i + times)%col_length] = val

    for i in range(col_length):
        grid[i][col] = new_col[i]
    return grid

def rotate_row(grid, row, times):
    row_length = len(grid[row])
    total_times = times % row_length
    a = grid[row][-total_times:]
    b = grid[row][:(row_length - total_times)]
    grid[row] =a + b
    return grid
    new_row = ['.'] * row_length
    for i in range(row_length):
        val = grid[i][col]
        new_col[(i + times)%col_length] = val

    for i in range(col_length):
        grid[i][col] = new_col[i]
    return grid


# rows = ['rect 3x2', 'rotate column x=1 by 1', 'rotate row y=0 by 4', 'rotate column x=1 by 1']
# grid = [["." for _ in range(7)] for _ in range(3)]
print(grid)
for row in rows:

    if 'rect' in row:
        r = row.replace("rect ", "")
        a, b = r.split("x")
        a,b = int(a), int(b)
        grid = create_rect(grid, a, b)
        print(grid)
    elif 'rotate row y=' in row:
        r = row.replace('rotate row y=', "")
        a,b = r.split(" by ")
        a,b = int(a), int(b)
        grid = rotate_row(grid, a, b)
        print(grid)

    elif 'rotate column x=' in row:
        r = row.replace('rotate column x=', "")
        a,b = r.split(" by ")
        a,b = int(a), int(b)
        grid = rotate_column(grid, a, b)
        print(grid)

print(grid)

print(sum([c.count("#") for c in grid]))

for r in grid:
    print(r)