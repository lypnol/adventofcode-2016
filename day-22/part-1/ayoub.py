from submission import Submission


class AyoubSubmission(Submission):

    def author(self):
        return 'Ayoub'

    def run(self, s):
        s = s.rstrip().split('\n')[2:]

        n = 31

        nodes = []
        i = -1
        j = 0
        for line in s:
            tokens = line.split()
            if j == 0:
                nodes.append([None for _ in range(n)])
                i += 1
            nodes[i][j] = (int(tokens[2][:-1]), int(tokens[3][:-1]))
            j = (j + 1) % n

        count = 0
        for i1 in range(n):
            for j1 in range(n):
                for i2 in range(n):
                    for j2 in range(n):
                        if nodes[i1][j1][0] > 0 and (i1 != i2 or j1 != j2)\
                        and nodes[i1][j1][0] <= nodes[i2][j2][1]:
                            count += 1

        return count
