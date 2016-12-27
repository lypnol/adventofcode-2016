from submission import Submission


class AyoubSubmission(Submission):

    def author(self):
        return 'Ayoub'

    def run(self, s):
        instructions = s.rstrip().split('\n')

        X = int(instructions[1].split()[1])
        Y = int(instructions[2].split()[1])

        M = X * Y

        b = list('{0:b}'.format(M))
        for i in range(len(b)):
            if i % 2 == 0:
                b[i] = '1'
            else:
                b[i] = '0'

        n = int(''.join(b), 2)
        if n < M:
            if len(b) % 2 == 0:
                b.append('1')
            else:
                b.append('0')
            n = int(''.join(b), 2)

        return n - M
