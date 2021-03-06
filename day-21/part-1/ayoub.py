from submission import Submission


class AyoubSubmission(Submission):

    def author(self):
        return 'Ayoub'

    def run(self, s):
        s = s.rstrip()
        a = list("abcdefgh")

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

        def rotate_l(a, x):
            p = a.index(x)
            if p >= 4:
                p += 1
            p += 1
            return rotate(a, -p)

        def reverse(a, i, j):
            l1 = a[:i]
            l2 = a[j+1:]
            l3 = a[i:j+1]
            return l1 + l3[::-1] + l2

        def move(a, i, j):
            e = a.pop(i)
            a.insert(j, e)
            return a

        for line in s.split('\n'):
            tokens = line.split()
            if tokens[0] == "swap":
                if tokens[1] == "position":
                    a = swap(a, int(tokens[2]), int(tokens[5]))
                elif tokens[1] == "letter":
                    a = swap(a, a.index(tokens[2]), a.index(tokens[5]))
            elif tokens[0] == "rotate":
                if tokens[1] in ["left", "right"]:
                    a = rotate(a, int(tokens[2]) if tokens[1] == "left" else -int(tokens[2]))
                else:
                    a = rotate_l(a, tokens[6])
            elif tokens[0] == "reverse":
                a = reverse(a, int(tokens[2]), int(tokens[4]))
            elif tokens[0] == "move":
                a = move(a, int(tokens[2]), int(tokens[5]))

        return "".join(a)
