from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input.txt'

with open(input_path, 'r') as f:
    text = f.read()
rows = text.replace(",", "").replace("+", "").split("\n")
def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


rows = [i.split(" ") for i in rows]
rows = [[int(j) if is_int(j) else j for j in i] for i in rows]

print(rows)

dic = {}
dic['a'] = 1
dic['b'] = 0
p = 0
while p>=0 and p<len(rows):
    row = rows[p]
    ins, val = row[0], row[1]
    if len(row) > 2:
        c = row[2]
    if ins == 'jio':
        if dic[val] == 1:
            p += c
            continue
    elif ins == 'jie':
        if dic[val] % 2 == 0:
            p += c
            continue
    elif ins == 'inc':
        dic[val] += 1
    elif ins == "tpl":
        dic[val] *=3
    elif ins == 'hlf':
        dic[val] /=2
    elif ins == 'jmp':
        p += int(val)
        continue
    p += 1

print(dic)



