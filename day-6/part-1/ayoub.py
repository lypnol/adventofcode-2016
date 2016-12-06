from submission import Submission

class AyoubSubmission(Submission):

    def author(self):
        return 'Ayoub'

    def run(self, s):
        s = s.rstrip()
        n = 8
        occ = [[ 0 for _ in range(26) ] for i in range(n)]

        for line in s.split("\n"):
            for i in range(n):
                occ[i][ord(line[i]) - ord('a')] += 1

        password = [ chr(ord('a') + max(enumerate(occ[i]), key=lambda x: x[1])[0]) for i in range(n) ]

        return "".join(password)
