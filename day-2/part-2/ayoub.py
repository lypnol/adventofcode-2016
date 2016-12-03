from submission import Submission

class AyoubSubmission(Submission):

    def author(self):
        return 'Ayoub'

    def run(self, s):
        pad = [
            [' ', ' ', '1', ' ', ' '],
            [' ', '2', '3', '4', ' '],
            ['5', '6', '7', '8', '9'],
            [' ', 'A', 'B', 'C', ' '],
            [' ', ' ', 'D', ' ', ' ']
        ]

        code = ''
        i, j = 2, 0   #starting position
        for line in s.split('\n'):
            for c in line:
                if c == 'U' and i > 0 and pad[i-1][j] != ' ':
                    i -= 1
                elif c == 'D' and i < 4 and pad[i+1][j] != ' ':
                    i += 1
                elif c == 'L' and j > 0 and pad[i][j-1] != ' ':
                    j -= 1
                elif c == 'R'  and j < 4 and pad[i][j+1] != ' ':
                    j += 1
            code += pad[i][j]

        return code
