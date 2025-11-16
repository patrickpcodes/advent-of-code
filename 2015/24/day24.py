from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input.txt'

with open(input_path, 'r') as f:
    text = f.read()
rows = text.split('\n')
rows = [int(i) for i in rows]
# rows.reverse()
print(rows)
print(sum(rows))

ans = []

max_num = sum(rows)//4
print(max_num)

def product(nums):
    if len(nums) == 0:
        return 1
    return nums[0] * product(nums[1:])

subsets = []
shortest = 99999

def subset_sums(nums, target, partial=[]):
    global subsets
    global shortest

    s = sum(partial)

    if s == target:
        if len(partial) == shortest:
            subsets.append(partial)
        elif len(partial)<shortest:
            subsets = []
            shortest = len(partial)
            subsets.append(partial)

    if s > target:
        return

    for i in range(len(nums)):
        n = nums[i]
        remaining = nums[i+1:]
        subset_sums(remaining, target, partial+[n])

subset_sums(rows, max_num)
# print(subset_sums)
print("l")

choice = []
lowest = 9999999999999999999999 # 'infinity'

for elem in subsets:
    tmp = product(elem)
    if tmp < lowest:
        choice = elem
        lowest = tmp

print (elem, lowest)
# def get_min_length(a, b, c):
#     return min(len(a), len(b), len(c))

# def try_balance(a, b, c, weights):
#     global ans
#     global min_length
#     if len(weights) == 0:
#         if sum(a) == sum(b) and sum(b)== sum(c) and sum(c) == max_num:
#             ans.append((a, b, c))
#             min_length = min(min_length, get_min_length(a, b, c))
#         return
#     if get_min_length(a, b, c) > min_length:
#         return
#     w = weights[0]
#     if sum(a) + w <= max_num:
#         try_balance(a + [w], b, c, weights[1:] )
#     if sum(b) + w <= max_num:
#         try_balance(a, b+[w], c, weights[1:] )
#     if sum(c) + w <= max_num:
#         try_balance(a, b, c+[w], weights[1:] )

# # try_balance([],[],[], rows)



# def get_lowest_qe(grouping):
#     a, b, c = len(grouping[0]), len(grouping[1]), len(grouping[2])
#     min_val = a
#     if b < min_val:
#         min_val = b
#     if c < min_val:
#         min_val = c
#     mins = []
#     vals = [a, b, c]
#     for i in range(len(vals)):
#         if vals[i] == min_val:
#             mins.append(grouping[i])

#     min_qe = 9999999999999
#     for a in mins:
#         prod = 1
#         for i in a:
#             prod *=i
#         if prod < min_qe:
#             min_qe = prod

#     return min_qe


# print(ans)
# print(get_lowest_qe(ans[0]))