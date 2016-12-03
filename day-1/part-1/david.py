from submission import Submission

class DavidSubmission(Submission):

    def author(self):
        return "David"

    def run(self, s):
        pos = {'x': 0, 'y': 0}
        current_angle = 90 # heading north

        for stage in s.split(', '):
            turn = stage[0]
            if turn == 'R':
                current_angle -= 90
            else:
                current_angle += 90

            cos = 0
            sin = 0
            if current_angle % 180 == 0:
                cos = 1 - 2*int(current_angle % 360 == 180)
            if current_angle % 180 == 90:
                sin = 1 - 2*int(current_angle % 360 == 270)


            steps = int(stage[1:])
            pos['x'] += steps*cos
            pos['y'] += steps*sin

        return (abs(pos['x']) + abs(pos['y']))
