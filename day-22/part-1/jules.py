from submission import Submission

class JulesSubmission(Submission):

    def author(self):
        return 'Jules'

    def run(self, s):

        nodes = []
        for nodeLine in s.strip().split('\n')[2:]:
            elements = filter(None,nodeLine.split(' '))
            nodes.append((int(elements[2][:-1]),int(elements[3][:-1]),elements[0]))

        byUsed = sorted(nodes, key=lambda x: x[0])
        byAvail = sorted(nodes, key=lambda x: x[1])

        pairs = 0
        i = len(byAvail)-1
        count = 0
        for el in byUsed[::-1]:
            if el[0] == 0:
                continue
            while el[0] <= byAvail[i][1] and i >= 0:
                if el[2] == byAvail[i][2]:
                    i -= 1
                else:
                    i -= 1
                    count += 1

            pairs += count

        return pairs