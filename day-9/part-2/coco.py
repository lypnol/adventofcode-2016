import re
from submission import Submission

class CocoDay9Part1(Submission):

    def author(self):
        return "coco"

    def run(self, instructions):
        return self.solve(instructions.strip())

    def solve(self, string):
        if len(string) <= 1:
            return len(string)
        elif string.startswith("("):
            m = re.match(r"^\(([0-9]+)x([0-9]+)\)", string)
            if m:
                x, y = m.groups()
                j = m.end()
                return int(y) * self.solve(string[j:j+int(x)]) + self.solve(string[j+int(x):])
            else:
                return 1 + self.solve(string[1:])
        else:
            return 1 + self.solve(string[1:])
