from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent
input_path = script_dir / 'input.txt'

with open(input_path, 'r') as f:
    text = f.read()


from re import search
rows = text.split("\n")


data = [
'123 -> x',
'456 -> y',
'x AND y -> d',
'x OR y -> e',
'x LSHIFT 2 -> f',
'y RSHIFT 2 -> g',
'NOT x -> h',
'NOT y -> i'
]

data = rows

wires={}

AND = ' AND '
OR = ' OR '
LSHIFT = ' LSHIFT '
RSHIFT = ' RSHIFT '
NOT = 'NOT'

for d in data:
    signal, wire = d.split(' -> ')
    wires[wire] = signal
#print(wires)

def solve(wire):
    if wire.isnumeric():
        return int(wire)

    signal = wires[wire]

    if type(signal) == int or signal.isnumeric():
        wires[wire] = int(signal)
    else:
        if AND in signal:
            a,b = signal.split(AND)
            wires[wire] = solve(a) & solve(b)
        elif OR in signal:
            a, b = signal.split(OR)
            wires[wire] = solve(a) | solve(b)

        elif LSHIFT in signal:
            a, b = signal.split(LSHIFT)
            wires[wire] = solve(a) << int(b)

        elif RSHIFT in signal:
            a, b = signal.split(RSHIFT)
            wires[wire] = solve(a) >> int(b)

        elif NOT in signal:
            _, a = signal.split()
            wires[wire] = ~(solve(a))
            '''
            Tilde (~n) operator is the bitwise negation operator:
            it takes the number n as binary number and “flips” all bits
            e.g. 0 to 1 and 1 to 0 to obtain the complement binary number.
            '''

        else:
            wires[wire] = solve(signal)

    return wires[wire]





print(solve('a'))

tmp = solve('a')
for d in data:
    signal, wire = d.split(' -> ')
    wires[wire] = signal
wires['b'] = tmp
print(solve('a'))


# print(solve('a'))


