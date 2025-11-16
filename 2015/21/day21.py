from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input.txt'

with open(input_path, 'r') as f:
    text = f.read()


lines = open(input_path).read().splitlines()
lines = [ l.split(' ') for l in lines]
from collections import namedtuple
BOSS_HIT_POINTS = int(lines[0][2]) # 104
BOSS_DAMAGE = int(lines[1][1]) # 8
BOSS_ARMOR = int(lines [2][1]) # 1

Item = namedtuple('Item', ['name', 'cost', 'dmg', 'armor'])

WEAPONS = [
    Item('Dagger',        8,     4,       0),
    Item('Shortsword',   10,     5,       0),
    Item('Warhammer',    25,     6,       0),
    Item('Longsword',    40,     7,       0),
    Item('Greataxe',     74,     8,       0),
]
ARMOR = [
    Item('Nothing',       0,     0,       0),
    Item('Leather',      13,     0,       1),
    Item('Chainmail',    31,     0,       2),
    Item('Splintmail',   53,     0,       3),
    Item('Bandedmail',   75,     0,       4),
    Item('Platemail',   102,     0,       5),
]

RINGS = [
    Item('Nothing 1',     0,     0,       0),
    Item('Nothing 2',     0,     0,       0),
    Item('Damage +1',    25,     1,       0),
    Item('Damage +2',    50,     2,       0),
    Item('Damage +3',   100,     3,       0),
    Item('Defense +1',   20,     0,       1),
    Item('Defense +2',   40,     0,       2),
    Item('Defense +3',   80,     0,       3),
]

HITPOINTS = 100

import itertools

choices = []
for i in range(len(WEAPONS)):
    for j in range(len(ARMOR)):
        for k in range(len(RINGS)-1):
            for l in range(k+1, len(RINGS)):
                gear = []
                gear.append(WEAPONS[i])
                gear.append(ARMOR[j])
                gear.append(RINGS[k])
                gear.append(RINGS[l])
                choices.append(gear)

print(choices)

def win_fight(dmg, armor):
    boss_hit = BOSS_HIT_POINTS
    hit = HITPOINTS
    while boss_hit > 0 and hit > 0:
        player_damage = max(dmg - BOSS_ARMOR, 1)
        boss_damage = max(BOSS_DAMAGE - armor, 1)
        hit -= boss_damage
        boss_hit -= player_damage
        # check boss first, simulates player playing first
        if boss_hit <= 0:
            return True
        if hit <=0:
            return False

min_cost = 100000
max_cost = 0
for choice in choices:
    w, a, r1, r2 = choice
    dmg = w.dmg + a.dmg + r1.dmg + r2.dmg
    armor = w.armor + a.armor + r1.armor + r2.armor
    cost = w.cost + a.cost + r1.cost + r2.cost
    res = win_fight(dmg, armor)
    if res:
        min_cost = min(min_cost, cost)
    else:
        max_cost = max(max_cost, cost)

print(min_cost)
print(max_cost)