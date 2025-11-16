from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input.txt'

with open(input_path, 'r') as f:
    text = f.read()


text = text.replace(": capacity ", " ")
text = text.replace(", durability ", " ")
text = text.replace(", flavor ", " ")
text = text.replace(", texture ", " ")
text = text.replace(", calories ", " ")
text = text.replace(" km/s for ", " ")
text = text.replace(" seconds, but then must rest for ", " ")
text = text.replace(" seconds.", "")
rows = text.split('\n')
print(rows)
ingredients = {}
info = []
for row in rows:
    r = row.split(" ")
    ingredients[r[0]] = (int(r[1]),int(r[2]),int(r[3]),int(r[4]),int(r[5]) )
    info.append([int(r[1]),int(r[2]),int(r[3]),int(r[4]),int(r[5])])

print(info)



scores = []
calorie = 500
for i in range(100):
    for j in range(100):
        if i + j > 100:
            break
        for k in range(100):
            if i + j + k > 100:
                break
            for l in range(100):
                if i + j + k + l > 100:
                    break
                if i + j + k + l != 100:
                    continue
                cal = info[0][4]*i + info[1][4]*j + info[2][4]*k + info[3][4] *l
                if cal != calorie: continue
                cap = info[0][0]*i + info[1][0]*j + info[2][0]*k + info[3][0] *l
                dur = info[0][1]*i + info[1][1]*j + info[2][1]*k + info[3][1] *l
                fla = info[0][2]*i + info[1][2]*j + info[2][2]*k + info[3][2] *l
                txt = info[0][3]*i + info[1][3]*j + info[2][3]*k + info[3][3] *l
                if cap < 1 or dur < 1 or fla <1 or txt<1: continue
                scores.append(cap*dur*fla*txt)

print(max(scores))