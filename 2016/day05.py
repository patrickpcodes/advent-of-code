from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input05.txt'

with open(input_path, 'r') as f:
    text = f.read()




import hashlib

# Part 1
# input = "wtnhxymk"
# first_5 = "00000"
# password= ""
# num = 0
# while len(password)< 8:
#     hashable = input + str(num)
#     md5_hash = hashlib.md5(hashable.encode("utf-8")).hexdigest()
#     h = md5_hash[:5]
#     if md5_hash[:5] == first_5:
#         password+=md5_hash[5]
#         print(password, num)
#     num += 1
# print(password)

#Part 2
input = "wtnhxymk"
# input = "abc"
first_5 = "00000"
password= ["_"] * 8
num = 0
print("".join(password))
while "_" in password:
    hashable = input + str(num)
    md5_hash = hashlib.md5(hashable.encode("utf-8")).hexdigest()
    h = md5_hash[:5]
    if md5_hash[:5] == first_5:
        pos  = md5_hash[5]
        if pos.isnumeric():
            if int(pos) < 8:
                if password[int(pos)]=="_":
                    password[int(pos)] = md5_hash[6]
                    print("".join(password))
    num += 1

print("".join(password))