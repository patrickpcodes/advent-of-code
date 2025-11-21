from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input09.txt'

with open(input_path, 'r') as f:
    text = f.read()

rows = text.split('\n')
print(text)
print(rows)

import re
pattern = re.compile(r"\((\d+)x(\d+)\)")


# result = ""
# current_code_text=""
# current_code_length=-1
# current_code_time = 1
# pos = 0

# # text = "A(2x2)BCD(2x2)EFG"
# while pos < len(text):
#     searchable_text = text[pos:]
#     m = pattern.search(searchable_text)
#     if not m:
#         result += searchable_text
#         break
#     if m.start() > 0:
#         result += searchable_text[: m.start()]
#     a, b = m.group(0).replace("(", "").replace(")", "").split("x")
#     a, b = int(a), int(b)
#     current_code_length = a
#     current_code_time = b
#     print(current_code_length, current_code_time)
#     print(m.end())
#     end = m.end() + a
#     current_code_text = searchable_text[m.end():end]
#     # result +=m.group(0)
#     result += current_code_text * b
#     pos += end

# print(result)
# print("ABCBCDEFEFG" == result)
# print(len(result))


## Part 2, just keep a count of deconstructed string

result_len = 0
current_code_text=""
current_code_length=-1
current_code_time = 1
pos = 0

#### Needs to be fully recursive as it goes through each.
####


# def get_expanded_length(text, times):
#     length = 0
#     m = pattern.search(searchable_text)
#     if not m:
#         return len(text) * times
#     if m.start() > 0:
#         length += m.start()
#     a, b = m.group(0).replace("(", "").replace(")", "").split("x")
#     a, b = int(a), int(b)



def get_expanded_length(text, times, inner = True):
    length = 0
    pos = 0
    while pos < len(text):
        searchable_text = text[pos:]
        m = pattern.search(searchable_text)
        if not m:
            length += len(searchable_text)
            break
        if m.start() > 0:
            length += m.start()
        a, b = m.group(0).replace("(", "").replace(")", "").split("x")
        a, b = int(a), int(b)
        current_code_length = a
        current_code_time = b
        end = m.end() + a
        # current_code_text = searchable_text[m.end():end]
        # result +=m.group(0)
        length += get_expanded_length(searchable_text[m.end():end], b)
        pos += end
    return length * times

# print(result)
# print("ABCBCDEFEFG" == result)
# print(len(result))

print(get_expanded_length("(27x12)(20x12)(13x14)(7x10)(1x12)A", 1))
print(get_expanded_length(text, 1))
# print(len("XABCABCABCABCABCABCY"))