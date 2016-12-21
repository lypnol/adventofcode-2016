from submission import Submission
from collections import defaultdict


class AyoubSubmission(Submission):
    d = set()

    def author(self):
        return 'Ayoub'

    def run(self, s):
        s = s.rstrip().split('\n')
        a = list("fbgdceah")
        c = list("bdfhgeca")

        def swap(a, i, j):
            t = a[i]
            a[i] = a[j]
            a[j] = t
            return a

        def rotate(a, p):
            b = ""
            for i in range(len(a)):
                j = (i + p) % len(a)
                b += a[j]
            return list(b)

        def reverse(a, i, j):
            l1 = a[:i]
            l2 = a[j+1:]
            l3 = a[i:j+1]
            return l1 + l3[::-1] + l2

        def move(a, i, j):
            e = a.pop(i)
            a.insert(j, e)
            return a

        def explore(a, c, i):
            if i == -1:
                if ''.join(c) == 'abcdefgh':
                    self.d.add(''.join(a))
                    print self.d
                return

            line = s[i]
            tokens = line.split()
            if tokens[0] == "swap":
                if tokens[1] == "position":
                    a = swap(list(a), int(tokens[5]), int(tokens[2]))
                    c = swap(list(c), int(tokens[5]), int(tokens[2]))
                elif tokens[1] == "letter":
                    a = swap(list(a), a.index(tokens[5]), a.index(tokens[2]))
                    c = swap(list(c), c.index(tokens[5]), c.index(tokens[2]))
            elif tokens[0] == "rotate":
                if tokens[1] in ["left", "right"]:
                    a = rotate(list(a), -int(tokens[2]) if tokens[1] == "left" else int(tokens[2]))
                    c = rotate(list(c), -int(tokens[2]) if tokens[1] == "left" else int(tokens[2]))
                else:
                    for x in range(8):
                        a = list(rotate(list(a), x))
                        c = list(rotate(list(c), x))
                        explore(a, c, i-1)
                    return
            elif tokens[0] == "reverse":
                a = reverse(list(a), int(tokens[2]), int(tokens[4]))
                c = reverse(list(c), int(tokens[2]), int(tokens[4]))
            elif tokens[0] == "move":
                x, y =  int(tokens[2]), int(tokens[5])
                a = move(list(a), )
                c = move(list(c), )

            explore(list(a), list(c), i-1)

        explore(a, c, len(s)-1)

        return self.d
