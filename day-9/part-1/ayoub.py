from submission import Submission
import re

class AyoubSubmission(Submission):

    def author(self):
        return 'Ayoub'

    def run(self, s):
        s = s.rstrip()
        count = len(s)
        for c in s:
            if c == " ":
                count -= 1

        i = 0
        while i < len(s):
            if s[i] == '(':
                m = re.match(r"^(?P<marker>\([0-9]*x[0-9]*\))", s[i:])
                if m and m.group('marker'):
                    marker = m.group('marker')
                    n, m = map(int, marker[1:-1].split('x'))
                    count -= len(marker)
                    count += n * (m - 1)
                    i += len(marker) + n
                    continue
            i += 1

        return count
