from submission import Submission

class AyoubSubmission(Submission):

    def author(self):
        return 'Ayoub'

    def run(self, s):

        x,y,o = 0,0,"N" # position and orientation
        commands = s.split(', ')

        for c in commands:
            direction = c[0]
            distance = int(c[1:])
            if o == "N":
                if direction == "R":
                    o = "E"
                    x += distance
                else:
                    o = "W"
                    x -= distance
            elif o == "S":
                if direction == "R":
                    o = "W"
                    x -= distance
                else:
                    o = "E"
                    x += distance
            elif o == "W":
                if direction == "R":
                    o = "N"
                    y += distance
                else:
                    o = "S"
                    y -= distance
            elif o == "E":
                if direction == "R":
                    o = "S"
                    y -= distance
                else:
                    o = "N"
                    y += distance

        return(abs(x)+abs(y))
