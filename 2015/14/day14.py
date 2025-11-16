from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input.txt'

with open(input_path, 'r') as f:
    text = f.read()


text = text.replace(" can fly ", " ")
text = text.replace(" km/s for ", " ")
text = text.replace(" seconds, but then must rest for ", " ")
text = text.replace(" seconds.", "")
rows = text.split('\n')
print(rows)

dic = {}
for row in rows:
    r = row.split(" ")
    dic[r[0]] = (int(r[1]), int(r[2]), int(r[3]))

print(dic)

def dist_in_flying_period(speed, length_at_speed):
    return speed * length_at_speed

def calculate_distance_after_seconds(speed, length_at_speed, rest_time, total_seconds):
    full_periods = total_seconds // (length_at_speed + rest_time)
    remaining_time = total_seconds % (length_at_speed + rest_time)
    dist = dist_in_flying_period(speed, length_at_speed) * full_periods
    if remaining_time >= length_at_speed:
        dist += dist_in_flying_period(speed, length_at_speed)
    else:
        dist += dist_in_flying_period(speed, remaining_time)
    return dist

max_dist = 0
total_seconds = 2503
for rein in dic.keys():
    a, b, c = dic[rein]
    dist = calculate_distance_after_seconds(a, b, c, total_seconds)
    if dist > max_dist:
        max_dist = dist
print(max_dist)



points = {}
positions = {}
for d in dic.keys():
    positions[d] = 0
    points[d] = 0

def get_leaders(positions):
    leaders = []
    lead = max(positions.values())
    for p in positions.keys():
        if positions[p] == lead:
            leaders.append(p)
    return leaders

def assign_points(points, leaders):
    for l in leaders:
        points[l] += 1
    return points

for i in range(1, total_seconds+1):
    for r in dic.keys():
        a, b, c = dic[r]
        positions[r] =calculate_distance_after_seconds(a, b, c, i)
    leaders = get_leaders(positions)
    points= assign_points(points, leaders)

print(max(points.values()))