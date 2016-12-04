from submission import Submission

pad = [
        [None, None, '1', None, None],
        [None,  '2', '3', '4' , None],
        [ '5',  '6', '7', '8' , '9' ],
        [None,  'A', 'B', 'C' , None],
        [None, None, 'D', None, None]
    ]

class DavidSubmission(Submission):
    def author(self):
        return 'David'

    def exists_pos(self, x, y):
        return pad[y][x] != None

    def follow_instructions(self, x, y, instructions):
        for instruction in instructions:
            if instruction == 'L' and x > 0 and self.exists_pos(x-1, y):
                x -= 1
            elif instruction == 'R' and x < 4 and self.exists_pos(x+1, y):
                x += 1
            elif instruction == 'U' and y > 0 and self.exists_pos(x, y-1):
                y -= 1
            elif instruction == 'D' and y < 4 and self.exists_pos(x, y+1):
                y += 1

        return {'x': x, 'y': y}

    def run(self, s):

        answer = ''
        pos = {'x': 0, 'y': 2}
        for instructions_line in s.strip().split('\n'):
            pos = self.follow_instructions(pos['x'], pos['y'], instructions_line)
            answer += pad[pos['y']][pos['x']]

        return answer
