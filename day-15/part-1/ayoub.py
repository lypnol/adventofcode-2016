from submission import Submission


class AyoubSubmission(Submission):

    def author(self):
        return 'Ayoub'

    def run(self, s):
        s = s.rstrip()

        D = []
        for line in s.split('\n'):
            tokens = line.split()
            D.append((int(tokens[3]), int(tokens[-1][:-1])))

        def is_good(x, D):
            for i, (P, A) in enumerate(D):
                if (x + A + i + 1) % P != 0:
                    return False
            return True

        x = 0
        while not is_good(x, D):
            x += 1

        return x
