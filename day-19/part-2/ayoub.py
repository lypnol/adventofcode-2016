from submission import Submission


class AyoubSubmission(Submission):

    def author(self):
        return 'Ayoub'

    def run(self, s):
        s = s.rstrip()
        n = int(s)

        p = 1
        while 3 * p <= n:
            p *= 3

        if n == p:
            return n

        return n - p + max(n - 2 * p, 0)
