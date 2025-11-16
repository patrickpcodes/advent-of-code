from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input.txt'

with open(input_path, 'r') as f:
    text = f.read()


data = "CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr"

dic = {}
rows = text.split("\n")
for row in rows:
    r = row.split("=>")
    a, b = r[0].strip(), r[1].strip()
    if a in dic:
        l = dic[a]
        l.append(b)
        dic[a] = l
    else:
        dic[a] = [b]
print(dic)


def get_replacements(input, output, data):
    new_strings = []
    start = 0
    s = data
    while True:
        i = s.find(input, start)
        if i == -1:
            break
        # replace JUST this one occurrence
        s = s[:i] + output + s[i + len(input):]

        new_strings.append(s)
        start = i + 1
        s = data

    return new_strings

strings = []
for item in dic:
    for vals in dic[item]:
        for val in vals:
            rep = get_replacements(item, vals, data)
            strings.extend(rep)

cl_strings = set(strings)
print(len(cl_strings))

rows = text.split("\n")
replacements = [(l.split()[-1], l.split()[0]) for l in rows if '=>' in l]
replacements.sort(key=lambda x: len(x[0])) # sort by string length
replacements = replacements[::-1] # reverse

print(replacements)
data = "CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr"
s = data
count = 0
print(f"Replacement Length is {len(replacements)}")
def try_replace(s, replacements):
    original_string = s
    for lhs, rhs in replacements:
        if lhs in original_string:
            s = original_string.replace(lhs, rhs, 1)
            if s == "e":
                return 1
            val = try_replace(s, replacements)
            if val > 0:
                return 1 + val
    return 0


# while s != "e":
#     for lhs, rhs in replacements:
#         if lhs in s:
#             s = s.replace(lhs, rhs, 1)
#             count += 1
#             break

print(try_replace(data, replacements))