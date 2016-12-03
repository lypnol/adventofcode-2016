
def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

valid = 0
read_lines = []
with open("input.txt") as f:
    for line in f:
        a, b, c = list(map(int, line.split()))
        read_lines += [[a, b, c]]
        if len(read_lines) == 3:
            for i in range(3):
                if is_triangle(read_lines[0][i], read_lines[1][i], read_lines[2][i]):
                    valid += 1
            read_lines = []
print(valid)
