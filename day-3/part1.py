
def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

valid = 0
with open("input.txt") as f:
    for line in f:
        a, b, c = list(map(int, line.split()))
        if is_triangle(a, b, c):
            valid += 1
print(valid)
