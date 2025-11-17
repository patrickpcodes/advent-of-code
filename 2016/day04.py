from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input04.txt'

with open(input_path, 'r') as f:
    text = f.read()

rows = text.split('\n')
# rows = ['aaaaa-bbb-z-y-x-123[abxyz]','a-b-c-d-e-f-g-h-987[abcde]' ]
full_letters = "abcdefghijklmnopqrstuvwxyz"

valid_ids = []

def generate_checksum(letters):
    count = {}
    letters = letters.replace("-", "")
    for i in letters:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    vals = []
    for j in count.keys():
        vals.append((j, count[j], full_letters.index(j)))

    vals = sorted(vals, key=lambda x :(-x[1], x[2]))
    code = [v[0] for v in vals]
    return "".join(code[:5])




def is_valid_room(letters, check_sum):
    chck = generate_checksum(letters)
    return chck == check_sum

def decrypt_name(letters, num):
    res = ""
    num = num % len(full_letters)
    for l in letters:
        if l == "-":
            res += " "
        else:
            res += full_letters[(full_letters.index(l)+num) % len(full_letters)]
    return res



for row in rows:
    code, check_sum = row.split('[')
    check_sum = check_sum[:-1]
    code_split = code.rsplit('-', 1)
    letters = "".join(code_split[0:-1])
    num = int(code_split[-1])
    if is_valid_room(letters, check_sum):
        valid_ids.append(int(num))
        valid_room = decrypt_name(letters, num)
        if "north" in valid_room and "pole" in valid_room:
            print(valid_room, num)


print(sum(valid_ids))


