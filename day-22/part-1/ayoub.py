from submission import Submission


class AyoubSubmission(Submission):

    def author(self):
        return 'Ayoub'

    def run(self, s):
        s = s.rstrip().split('\n')[2:]

        nodes = []
        for line in s:
            tokens = line.split()
            nodes.append((int(tokens[2][:-1]), int(tokens[3][:-1])))

        n = len(nodes)

        pairs = set()
        for i in range(n):
            for j in range(n):
                if i != j and nodes[i][0] > 0  \
                and nodes[i][0] <= nodes[j][1] \
                and (j, i) not in pairs:
                    pairs.add((i, j))

        return len(pairs)
