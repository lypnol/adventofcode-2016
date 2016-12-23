from submission import Submission

class CocoDay12Part1(Submission):


    def author(self):
        return "coco"

    def number_to_binary(self, n):
        return "{0:b}".format(n)

    def is_open(self, x, y):
        somme = x*x + 3*x + 2*x*y + y + y*y + self.n
        binary = self.number_to_binary(somme)
        return sum(1 for c in binary if c == '1') % 2 == 0

    def get_possible_neighbours(self, x, y):
        possible = [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]
        possible = [(x,y) for (x, y) in possible if x >= 0 and y >= 0 and self.is_open(x, y)]
        return possible

    def run(self, instructions):
        total_steps = 50
        self.n = int(instructions.strip())
        visited = set()
        to_visit = {(1, 1)}
        steps = 0
        while steps <= 50:
            to_visit_copy = [a for a in to_visit]
            to_visit = set()
            for (x1, y1) in to_visit_copy:
                neighbours = self.get_possible_neighbours(x1, y1)
                [to_visit.add(n) for n in neighbours] # we add them in to_visit
                visited.add((x1, y1))
            steps += 1
        return len(visited)
