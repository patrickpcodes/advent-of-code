from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input02.txt'

with open(input_path, 'r') as f:
    text = f.read()

#text = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

rows = text.split(',')

def is_item_repeated_twice(s):
    if len(s) %2 != 0:
        return False
    m = len(s) //2
    return s[:m] == s[m:]

sum = 0
for r in rows:
    s, e = r.split("-")
    s, e = int(s), int(e)
    for i in range(s, e+1):
        if is_item_repeated_twice(str(i)):
            sum += i


print(sum)


def is_only_substring(sub, s):
    # if len(s) % len(sub) != 0:
    #     return False
    times = len(s) // len(sub)
    return sub * times == s

def is_id_invalid_2(s):
    for i in range(1, len(s) ):
        if is_only_substring(s[:i], s[i:]):
            return True
    return False

# text = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

# rows = text.split(',')

sum = 0
for r in rows:
    s, e = r.split("-")
    s, e = int(s), int(e)
    for i in range(s, e+1):
        if is_id_invalid_2(str(i)):
            sum += i
print(sum)