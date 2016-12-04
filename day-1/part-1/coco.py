from submission import Submission

class CocoDay1Part1(Submission):

    def author(self):
        return"coco"

    def run(self, instructions):
        instructions = [instruction.strip() for instruction in instructions.split(",")]
        x = 0
        y = 0
        direction = 0

        for instruction in instructions:
            turn = instruction[0]
            length = instruction[1:]
            if turn == "R":
                direction = (direction + 1) % 4
            elif turn == "L":
                direction = (direction - 1) % 4
            if direction == 0:
                y += int(length)
            elif direction == 1:
                x += int(length)
            elif direction == 2:
                y -= int(length)
            elif direction == 3:
                x -= int(length)
        return(abs(x) + abs(y))
