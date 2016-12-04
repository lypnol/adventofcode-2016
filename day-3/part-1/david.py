from submission import Submission

class DavidSubmission(Submission):
    def author(self):
        return 'David'

    def is_valid_triangle(self,edges):
        # print(sorted(edges))
        x, y, z = tuple(sorted(edges))
        return z < x + y

    def run(self, triangles):

        count = 0
        for triangle in triangles.strip().split('\n'):
            edges = [int(x) for x in triangle.strip().split()]
            if self.is_valid_triangle(edges):
                count += 1

        return str(count)
