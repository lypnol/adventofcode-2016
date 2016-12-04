from submission import Submission

class CocoDay3Part1(Submission):

    def author(self):
        return"coco"

    def run(self, instructions):
        n = 0
        for line in instructions.strip().split("\n"):
            sides = [int(x) for x in line.split()]
            somme = sum(sides)
            if all(somme - x > x for x in sides):
                n += 1
        return n
