from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input.txt'

with open(input_path, 'r') as f:
    text = f.read()

text = text.replace(" would gain ", " ")
text = text.replace(" would lose ", " -")
text = text.replace(" happiness units by sitting next to ", " ")
text = text.replace(".", " ")
rows = text.split('\n')

print (rows)

seats = {}
people = []
for row in rows:
    d = row.split(" ")
    a, val, b = d[0], int(d[1]), d[2]
    seats[a+b] = val
    people.append(a)
    people.append(b)

import itertools
people = set(people)
def get_best(people):
    best_change = 0

    for arrangement in itertools.permutations(people):
        second_list = []
        a_total = 0
        for a, b in zip( arrangement , arrangement[-1:] + arrangement[:-1]):
            a_total += seats[a+b]
            a_total += seats[b+a]
        if a_total > best_change:
            best_change = a_total
            # print(a_total)
    print(f"Best change for {len(people)} people is {best_change}")
    return people

get_best(people)

for p in people:
    seats[p+"NOBODY"] = 0
    seats["NOBODY"+p]=0

people.add("NOBODY")
get_best(people)