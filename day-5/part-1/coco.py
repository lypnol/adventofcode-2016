from submission import Submission
import hashlib

class CocoDay5Part1(Submission):

    def author(self):
        return "coco"

    def run(self, instructions):
        puzzle_input = instructions.strip()
        digest = ""
        password = ""
        index = 0
        for i in range(8):
            while not digest.startswith("00000"):
                digest = hashlib.md5(puzzle_input + str(index)).hexdigest()
                index += 1
            self.debug(index)
            password += digest[5]
            digest = ""
        return password
