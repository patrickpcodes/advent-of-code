from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input1.txt'

with open(input_path, 'r') as f:
    text = f.read()

def contains_num_of_items(txt, items, num):
    total = 0
    for t in txt:
        if t in items:
            total += 1
    return total >= num
    # for i in items:
    #     if i in txt:
    #         total +=1
    #         if total >= num:
    #             return True
    # return False

def contains_repeated_letter(txt):
    for i in txt:
        if i + i in txt:
            return True
    return False

def contains_string_in_list(txt, items):
    for item in items:
        if item in txt:
            return True
    return False

text = text.split('\n')
nice_count = 0
vowels = ['a', 'e', 'i', 'o', 'u']
bad_strings = ['ab', 'cd', 'pq', 'xy']
# text = ['aaa']
for t in text:
    if contains_num_of_items(t, vowels, 3) and contains_repeated_letter(t) and not contains_string_in_list(t, bad_strings):
        nice_count+=1

print(nice_count)
from re import search
nicer_count = 0
def pair_twice_no_overlap(text):
    return search(r"(..).*\1", text)


def repeated_one_space(text):
    for a, b in zip(text, text[2:]):
        if a == b:
            return True
    return False
print(sum(1 for t in text if pair_twice_no_overlap(t) and repeated_one_space(t)))