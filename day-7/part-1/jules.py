from submission import Submission

class JulesSubmission(Submission):

    def author(self):
        return 'Jules'

    def hasPalindrome(self,part):
        for i in range(len(part)-3):
            el = part[i:i+4]
            if el == el[::-1] and el[0] != el[1]:
                return True
        return False

    def supportsTLS(self,line):
        import re
        m = re.findall("([a-z]+)",line)
        hasOneOutside = False
        for i in range(0,len(m)-2,2):
            if self.hasPalindrome(m[i+1]):
                return False
            if self.hasPalindrome(m[i]):
                hasOneOutside = True
        return hasOneOutside or self.hasPalindrome(m[-1])

    def run(self, s):
        count = 0
        for line in s.strip().split('\n'):
            if self.supportsTLS(line):
                count += 1
        return count
