from submission import Submission
import re

class AyoubSubmission(Submission):

    def author(self):
        return 'Ayoub'

    def run(self, s):
        s = s.rstrip()

        def containsTLS(a):
            n = len(a)
            for i in range(n-3):
                if a[i] == a[i+3] and a[i+1] == a[i+2] and a[i] != a[i+1]:
                    return True
            return False

        count = 0
        for a in s.split('\n'):
            foundInBrakets = False
            for b in re.findall(r'\[.*?\]', a):
                foundInBrakets = containsTLS(b[1:-1])
                if foundInBrakets:
                    break
            if not foundInBrakets:
                for x in re.split(r'\[.*?\]', a):
                    if containsTLS(x):
                        count += 1
                        break
        return count
