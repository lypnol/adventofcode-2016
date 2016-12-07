from submission import Submission
import re

class AyoubSubmission(Submission):

    def author(self):
        return 'Ayoub'

    def run(self, s):
        s = s.rstrip()

        def containsSSL(b, subnets):
            n = len(b)
            for i in range(n-2):
                if b[i] == b[i+2] and b[i] != b[i+1]:
                    x, y = b[i], b[i+1]
                    for a in subnets:
                        if "".join([y, x, y]) in a:
                            return True
            return False

        count = 0
        for a in s.split('\n'):
            found = False
            subnets = re.split(r'\[.*?\]', a)
            for b in re.findall(r'\[.*?\]', a):
                found = containsSSL(b[1:-1], subnets)
                if found:
                    break
            if found:
                count += 1

        return count
