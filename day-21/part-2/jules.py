from submission import Submission

class JulesSubmission(Submission):

    def author(self):
        return 'Jules'

    def run(self, s):

        #Functions are strange because they're modified to do the inverse of what's meant by the instruction
        
        def swapPos(x,y,s):
            if x < y:
                return s[:x]+s[y]+s[x+1:y]+s[x]+s[y+1:]
            else:
                return s[:y]+s[x]+s[y+1:x]+s[y]+s[x+1:]

        def swapLetters(x,y,s):
            s = s.replace(x,"#")
            s = s.replace(y,x)
            return s.replace("#",y)

        def normal_rotateLR(dir,nb,s):
            nb = nb % len(s)
            if dir == "right":
                return s[-nb:]+s[:-nb]
            elif dir == "left":
                return s[nb:]+s[:nb]

        def normal_rotate(letter,s):
            pos = s.index(letter)
            if pos >= 4:
                nb = pos+2
            else:
                nb = pos+1
            return normal_rotateLR("right",nb,s)

        #Didn't figure out the right inversion of rotate, my head was sleepy. so until fix, I'll BF the rotations
        from itertools import permutations

        def rotateLR(dir,nb,s):
            for p in permutations(s):
                if normal_rotateLR(dir,nb,''.join(p)) == s:
                    return ''.join(p)

        def rotate(letter,s):
            for p in permutations(s):
                if normal_rotate(letter,''.join(p)) == s:
                    return ''.join(p)

        def reverse(x,y,s):
            subStr = s[x:y+1]
            return s[:x]+subStr[::-1]+s[y+1:]

        def move(xNew,yNew,s):
            x = yNew
            y = xNew
            if x < y:
                return s[:x]+s[x+1:y+1]+s[x]+s[y+1:]
            else:
                return s[:y]+s[x]+s[y:x]+s[x+1:]

        instructions = s.strip().split('\n')
        s = "fbgdceah"

        for instr in instructions[::-1]:
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


