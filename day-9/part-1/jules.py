from submission import Submission

class JulesSubmission(Submission):

    def author(self):
        return 'Jules'

    def run(self, s):
        count = 0
        length = len(s.strip())
        i = 0
        while i < length:
            if s[i] == '(':
                x = s.find("x",i)
                close = s.find(")",x)
                a = int(s[i+1:x])
                b = int(s[x+1:close])
                count += a*b
                i = close + a + 1
                continue
            count += 1
            i+= 1
        return count