from submission import Submission

class DavidSubmission(Submission):
    def author(self):
        return 'David'

    def is_valid_triangle(self,edges):
        # print(sorted(edges))
        x, y, z = tuple(sorted(edges))
        return z < x + y

    def run(self, input):
        lines = input.strip().split('\n')

        count = 0
        for index in xrange(0, len(lines), 3):
            triangles = []
            lines_batch = [line.strip().split() for line in lines[index:index+3]]
            for i in range(3):
                triangles.append([lines_batch[j][i] for j in range(3)])

            for triangle in triangles:
                edges = [int(x) for x in triangle]
                if self.is_valid_triangle(edges):
                    count += 1

        return str(count)
