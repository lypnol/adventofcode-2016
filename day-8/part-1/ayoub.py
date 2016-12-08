from submission import Submission
import re

class AyoubSubmission(Submission):

    def author(self):
        return 'Ayoub'

    def run(self, s):
        s = s.rstrip()

        h = 6
        w = 50
        def rotate(lst, x):
            x = x % len(lst)
            copy = list(lst)
            for i in range(len(lst)):
                if x<0:
                    lst[i+x] = copy[i]
                else:
                    lst[i] = copy[i-x]

        def rect(screen, A, B):
            for x in range(A):
                for y in range(B):
                    screen[y][x] = '#'

        def rotate_row(screen, A, B):
            rotate(screen[A], B)

        def rotate_col(screen, A, B):
            col = [None for _ in range(h)]
            for y in range(h):
                col[y] = screen[y][A]
            rotate(col, B)
            for y in range(h):
                screen[y][A] = col[y]

        screen = [['.' for x in range(w)] for y in range(h)]
        for line in s.split('\n'):
            tokens = line.split()
            command = tokens[0]
            if command == 'rect':
                A, B = map(int, tokens[1].split('x'))
                rect(screen, A, B)
            elif command == 'rotate' and tokens[1] == 'row':
                A, B = int(tokens[2].split('=')[1]), int(tokens[-1])
                rotate_row(screen, A, B)
            else:
                A, B = int(tokens[2].split('=')[1]), int(tokens[-1])
                rotate_col(screen, A, B)

        count = 0
        for y in range(h):
            for x in range(w):
                if screen[y][x] == '#':
                    count += 1

        return count
