from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input.txt'

with open(input_path, 'r') as f:
    text = f.read()


import re
rows = text.split("\n")

letters = "abcdefghijklmnopqrstuvwxyz"
bad = ['l', 'o', 'i']

def has_two_different_non_overlapping_pairs(p):
    found_first = ""
    for i in range(len(p)-1):
        a, b = p[i], p[i+1]
        if a == b:
            if found_first == "":
                found_first = a
            elif a != found_first:
                return True

    return False

def has_increasing_letters(p):
    for i in range(len(p)-2):
        a, b, c = p[i], p[i+1], p[i+2]
        if letters.index(b) == letters.index(a)+1 and letters.index(c) == letters.index(b) +1:
            return True
    return False

def get_next_pass(p):
    if p == "":
        return ""
    if p[len(p)-1] == "z":
        return get_next_pass(p[:-1]) + "a"
    else:
        return p[:-1] + letters[letters.index(p[len(p)-1])+1]

def is_valid(p):
    for b in bad:
        if b in p:
            return False
    if not has_two_different_non_overlapping_pairs(p):
        return False
    if not has_increasing_letters(p):
        return False
    return True

test = ["abcde","aabdddb", "aaajkl", "bbbbbbbbwwwwwwxyz"]
for t in test:
    print(f"Is {t} valid : {has_increasing_letters(t)}")
    print(get_next_pass(t))

start = "cqjxjnds"

while not is_valid(start):
    start = get_next_pass(start)

print(start)
start = get_next_pass(start)
while not is_valid(start):
    start = get_next_pass(start)

print(start)