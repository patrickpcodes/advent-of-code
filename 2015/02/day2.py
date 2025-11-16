from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input_1.txt'

with open(input_path, 'r') as f:
    text = f.read()

text = text.strip().split('\n')
total = 0

def area_smallest_side(x,y,z):
    maxi = max(x,y,z)
    return x * y * z / maxi

def perimeter_smallest_side(x,y,z):
    maxi = max(x,y,z)
    return (2*(x+y+z-maxi))

ribbon = 0

for line in text:
    x,y,z = line.split("x")
    x = int(x)
    y = int(y)
    z = int(z)
    mini = min(z, y, x)
    area = 2 * (x*y + x*z + y*z)
    area += area_smallest_side(x,y,z)
    # print(area)
    total += area
    rib = z * y * x
    rib += perimeter_smallest_side(x,y,z)
    ribbon += rib


print("Total")
print(total)
print("Ribbon")
print(ribbon)
