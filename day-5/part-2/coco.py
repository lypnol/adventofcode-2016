from submission import Submission
import hashlib

class CocoDay5Part1(Submission):

    def author(self):
        return "coco"

    def run(self, instructions):
        puzzle_input = instructions.strip()
        digest = ""
        index = 0
        code = {}
        while len(code) < 8:
            while not digest.startswith("00000"):
                digest = hashlib.md5(puzzle_input + str(index)).hexdigest()
                index += 1
            self.debug(index)
            position = digest[5]
            letter = digest[6]
            print(digest)
            if position not in code and position in map(str, [0,1,2,3,4,5,6,7]):
                code[position] = letter
                print(code)
            digest = ""
        return "".join(code[str(i)] for i in range(8))
