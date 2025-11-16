input = "ckczppom"

import hashlib


first_5 = "000000"
num = 1
while True:
    hashable = input + str(num)
    md5_hash = hashlib.md5(hashable.encode("utf-8")).hexdigest()
    leading_hash = md5_hash[0:6]
    if md5_hash[0:6] == first_5:
        print(num)
    else:
        num += 1