from submission import Submission
import hashlib


class AyoubSubmission(Submission):

    def author(self):
        return 'Ayoub'

    def run(self, s):
        s = s.rstrip()

        def get_next(i, j, path):
            h = hashlib.md5(s + ''.join(path)).hexdigest()
            is_open = ['b', 'c', 'd', 'e', 'f']
            n = []
            if i > 0 and h[0] in is_open:
                n.append((i-1, j, 'U'))
            if i < 3 and h[1] in is_open:
                n.append((i+1, j, 'D'))
            if j > 0 and h[2] in is_open:
                n.append((i, j-1, 'L'))
            if j < 3 and h[3] in is_open:
                n.append((i, j+1, 'R'))

            return n

        def explore(i=0, j=0, path=[]):
            if i == 3 and j == 3:
                return ''.join(path)
            sp = ''.join([' ' for _ in range(1000)])
            for u, v, m in get_next(i, j, path):
                p = explore(u, v, list(path) + [m])
                if len(sp) > len(p):
                    sp = p

            return sp

        return explore()
