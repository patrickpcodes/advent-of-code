from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input07.txt'

with open(input_path, 'r') as f:
    text = f.read()

rows = text.split()

import re

pattern = re.compile(r'([a-zA-Z])(?!\1)([a-zA-Z])\2\1')

import re

def has_abba(data):
    for d in data:
        matches = pattern.findall(d)
        if len(matches) > 0:
            return True
    return False

aba_pattern = re.compile(r'([a-zA-Z])(?!\1)([a-zA-Z])\1')

def get_aba_patter(text):
    matches = []
    for i in range(len(text)-2):
        if text[i] == text[i+2]:
            matches.append(text[i:i+3])
    return matches


def has_aba(inside, outside):
    matches = []
    for out in outside:
        matches += get_aba_patter(out)
    print(matches)
    to_find = [m[1]+m[0]+m[1] for m in matches]
    print(to_find)
    for i in inside:
        for t in to_find:
            if t in i:
                return True
    return False


abba_count = 0
aba_count = 0
# rows = ['zazbz[bzb]cdb']
for row in rows:
    inside = re.findall(r'\[([^\]]+)\]', row)     # ['bb', 'dd']
    outside = re.split(r'\[[^\]]+\]', row)        # ['aaa', 'ccc', 'eee']
    if has_abba(outside) and not has_abba(inside):
        abba_count += 1
    if has_aba(inside, outside):
        aba_count +=1

print(abba_count)
print(aba_count)


