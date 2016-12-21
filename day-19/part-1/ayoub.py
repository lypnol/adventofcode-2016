from submission import Submission


class AyoubSubmission(Submission):

    def author(self):
        return 'Ayoub'

    def run(self, s):
        s = s.rstrip()
        n = int(s)

        # used https://en.wikipedia.org/wiki/Josephus_problem

        b = "{0:b}".format(n)
        l = n - 2**(len(b) - 1)

        return 2 * l + 1
