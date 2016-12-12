import re
from submission import Submission

class CocoDay9Part1(Submission):

    def author(self):
        return "coco"

    def run(self, instructions):
        result = ""
        i = 0
        while i < len(instructions):
            m = re.match(r"^\(([0-9]*)x([0-9]*)\)", instructions[i:])
            if m:
                x, y = m.groups()
                j = m.end()
                result += (instructions[i+j:i+j+int(x)]) * int(y)
                i += j + int(x)
            else:
                result += instructions[i]
                i += 1
        return len(result.strip())
