from submission import Submission
import re

class AyoubSubmission(Submission):

    def author(self):
        return 'Ayoub'

    def run(self, s):
        s = s.rstrip()

        def decompress(x):
            if len(x) <= 1:
                return len(x)
            if x[0] == ' ':
                return 0
            if x[0] == '(':
                m = re.match(r"^(?P<marker>\([0-9]*x[0-9]*\))", x)
                if m and m.group('marker'):
                    marker = m.group('marker')
                    n, m = map(int, marker[1:-1].split('x'))
                    return m * decompress(x[len(marker):len(marker)+n]) + \
                           decompress(x[len(marker)+n:])

            return 1 + decompress(x[1:])

        return decompress(s)
