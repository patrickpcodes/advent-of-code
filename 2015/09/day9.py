from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input.txt'

with open(input_path, 'r') as f:
    text = f.read()


import re
rows = text.split("\n")
locations = []
path = {}
for row in rows:
    d = row.split(" ")
    city1 = d[0]
    city2 = d[2]
    distance = int(d[4])

    path[city1+city2] = distance
    path[city2+city1] = distance
    locations.append(city1)
    locations.append(city2)

locations = set(locations)

import itertools

shortest_path = 999999
longest_path = 0
for route in itertools.permutations(locations):
    route_path = 0
    for city1, city2 in zip(route[:-1], route[1:]):
        route_path += path[city1+city2]
    if route_path < shortest_path:
        shortest_path = route_path
    if route_path > longest_path:
        longest_path = route_path
print(shortest_path)
print(longest_path)

