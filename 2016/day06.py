from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input06.txt'

with open(input_path, 'r') as f:
    text = f.read()

rows = text.split()

pos_count = {}
for row in rows:
    for i in range(len(row)):
        if i not in pos_count:
            pos_count[i] = {}

        val = row[i]
        if val in pos_count[i]:
            pos_count[i][val] += 1
        else:
            pos_count[i][val] = 1

print(pos_count)

def get_max_letter(dic):
    maxi = 0
    max_letter = ""
    for key in dic.keys():
        if dic[key] > maxi:
            maxi = dic[key]
            max_letter = key
    return max_letter

def get_min_letter(dic):
    mini = 9999999
    min_letter = ""
    for key in dic.keys():
        if dic[key] < mini:
            mini = dic[key]
            min_letter = key
    return min_letter


maxi = ""
mini = ""
for i in range(len(rows[0])):
    dic = pos_count[i]
    maxi += get_max_letter(dic)
    mini += get_min_letter(dic)

print(maxi)
print(mini)

