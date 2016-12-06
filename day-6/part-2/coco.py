from collections import defaultdict
from submission import Submission

class CocoDay6Part1(Submission):

    def author(self):
        return "coco"

    def run(self, instructions):
        most_common_by_positions = []
        for line in instructions.strip().split("\n"):
            for i, char in enumerate(line):
                if len(most_common_by_positions) <= i :
                    characters = defaultdict(int)
                    characters[char] += 1
                    most_common_by_positions.append(characters)
                else:
                    most_common_by_positions[i][char] += 1
        answer = ""
        for d in most_common_by_positions:
            inverse = [(value, key) for key, value in d.items()]
            answer +=  min(inverse)[1]
        return answer
