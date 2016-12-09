from submission import Submission

class JulesSubmission(Submission):

    def author(self):
        return 'Jules'

    def run(self, s):

        def howMuch(s):
            length = len(s.rstrip())
            i = 0
            count = 0
            while i < length:
                if s[i] == '(':
                    x = s.find("x",i)
                    close = s.find(")",x)
                    a = int(s[i+1:x])
                    b = int(s[x+1:close])
                    count += howMuch(s[close+1:close+a+1])*b
                    i = close + a + 1
                    continue
                count += 1
                i+= 1
            return count

        return howMuch(s)