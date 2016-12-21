from submission import Submission

class JulesSubmission(Submission):

    def author(self):
        return 'Jules'

    def run(self, s):
        
        def swapPos(x,y,s):
            if x < y:
                return s[:x]+s[y]+s[x+1:y]+s[x]+s[y+1:]
            else:
                return s[:y]+s[x]+s[y+1:x]+s[y]+s[x+1:]

        def swapLetters(x,y,s):
            s = s.replace(x,"#")
            s = s.replace(y,x)
            return s.replace("#",y)

        def rotateLR(dir,nb,s):
            nb = nb % len(s)
            if dir == "right":
                return s[-nb:]+s[:-nb]
            elif dir == "left":
                return s[nb:]+s[:nb]

        def rotate(letter,s):
            pos = s.index(letter)
            if pos >= 4:
                nb = pos+2
            else:
                nb = pos+1
            return rotateLR("right",nb,s)

        def reverse(x,y,s):
            subStr = s[x:y+1]
            return s[:x]+subStr[::-1]+s[y+1:]

        def move(x,y,s):
            if x < y:
                return s[:x]+s[x+1:y+1]+s[x]+s[y+1:]
            else:
                return s[:y]+s[x]+s[y:x]+s[x+1:]

        instructions = s.strip().split('\n')
        s = "abcdefgh"

        for instr in instructions:
            elements = instr.split(' ')
            if elements[0] == "move":
                s = move(int(elements[2]),int(elements[5]),s)
            elif elements[0] == "swap":
                if elements[1] == "position":
                    s = swapPos(int(elements[2]),int(elements[5]),s)
                else:
                    s = swapLetters(elements[2],elements[5],s)
            elif elements[0] == "rotate":
                if elements[1] == "based":
                    s = rotate(elements[6],s)
                else:
                    s = rotateLR(elements[1],int(elements[2]),s)
            elif elements[0] == "reverse":
                s = reverse(int(elements[2]),int(elements[4]),s)

        return s

