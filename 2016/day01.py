from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input01.txt'

with open(input_path, 'r') as f:
    text = f.read()

directions = text.split(",")
directions = [i.strip() for i in directions]

print(directions)

current_direction = "N"
current_location = (0, 0)

l_dict = {
    "N":"W",
    "E":"N",
    "S":"E",
    "W":"S"
}
r_dict = {
    "N":"E",
    "E":"S",
    "S":"W",
    "W":"N"
}

visited_locations = [(0,0)]
found = False

def move(num, save_each_location=False):
    global current_location
    global visited_locations
    global found
    for i in range(num):
        if current_direction == "N":
            current_location = (current_location[0], current_location[1] + 1)
        if current_direction == "S":
            current_location = (current_location[0], current_location[1] - 1)
        if current_direction == "W":
            current_location = (current_location[0] - 1, current_location[1])
        if current_direction == "E":
            current_location = (current_location[0]+ 1, current_location[1] )
        if current_location in visited_locations:
            print("First Visited At ", current_location)
            found = True
            break
        visited_locations.append(current_location)


for d in directions:
    orientation, dist = d[0], int(d[1:])
    current_direction = l_dict[current_direction] if orientation == "L" else r_dict[current_direction]
    move(dist, True)
    if found:
        break

print(current_location)
print(abs(current_location[0]) + abs(current_location[1]))