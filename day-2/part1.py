
pad = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]

code = ''
i, j = 1, 1   #starting position
with open("input.txt") as f:
    for line in f:
        for c in line:
            if c == 'U' and i > 0:
                i -= 1
            elif c == 'D' and i < 2:
                i += 1
            elif c == 'L' and j > 0:
                j -= 1
            elif c == 'R'  and j < 2:
                j += 1
        code += pad[i][j]

print(code)
