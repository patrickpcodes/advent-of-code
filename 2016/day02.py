from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input02.txt'

with open(input_path, 'r') as f:
    text = f.read()

rows = text.split('\n')

combination = ""

grid = [[1,2,3],[4,5,6],[7,8,9]]
grid = [['X', 'X', 1 , 'X', 'X'],
        ['X',2,3,4, 'X'],
        [5,6,7, 8, 9],
        ['X', 'A', 'B', 'C', 'X'],
        ['X', 'X', 'D', 'X', 'X']]
def is_next_cell_valid(cell, x_change, y_change):
    global grid
    return grid[cell[0] + x_change][cell[1] + y_change] != "X"


def determine_key_for_row(row):
    global combination
    global grid
    current_cell = [1,1]
    for i in row:
        if i == "U":
            if current_cell[0] > 0:
                if is_next_cell_valid(current_cell, -1, 0):
                    current_cell[0] -= 1
        if i == "D":
            if current_cell[0] < len(grid)-1:
                if is_next_cell_valid(current_cell, 1, 0):
                    current_cell[0] += 1
        if i == "L":
            if current_cell[1] > 0:
                if is_next_cell_valid(current_cell, 0, -1):
                    current_cell[1] -= 1
        if i == "R":
            if current_cell[1] < len(grid[0])-1:
                if is_next_cell_valid(current_cell, 0, 1):
                    current_cell[1] += 1
    combination += str(grid[current_cell[0]][current_cell[1]])

for row in rows:
    determine_key_for_row(row)

print(combination)