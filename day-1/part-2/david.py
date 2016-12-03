import numpy as np
from submission import Submission

class DavidSubmission(Submission):
    def author(self):
        return 'David'

    def run(self, string):
        visited = [(0,0)]

        # turn left matrix
        #   0 (-1)
        #   1   0
        turn_left = np.array([[0,-1], [1,0]])

        # turn right matrix
        #
        #   0  1
        #  -1  0
        turn_right = np.array([[0,1], [-1,0]])

        direction = np.array([0,1]) # North

        for instruction in string.split(', '):
            turn = instruction[0]
            if turn == 'L':
                direction = turn_left.dot(direction)
            else:
                direction = turn_right.dot(direction)

            steps = int(instruction[1:])
            for _ in range(steps):
                pos = visited[-1]
                pos = map(lambda x, y:x+y, tuple(direction), pos)
                if pos in visited:
                    return (abs(pos[0]) + abs(pos[1]))
                visited.append(pos)
