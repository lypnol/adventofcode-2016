from submission import Submission

class JulesSubmission(Submission):

    def author(self):
        return 'Jules'

    def hasPalindrome(self,part):
        els = []
        for i in range(len(part)-2):
            el = part[i:i+3]
            if el == el[::-1] and el[0] != el[1]:
                els.append(el)
        return els

    def inverse(self,el):
        return el[1]+el[0]+el[1]

    def supportsSSL(self,line):
        import re
        m = re.findall("([a-z]+)",line)
        tripletInBrackets = []
        tripletOutsideBrackets = []
        for i in range(0,len(m)-2,2):
            pal = self.hasPalindrome(m[i+1])
            if len(pal) != 0:
                tripletInBrackets.extend(pal)
            pal = self.hasPalindrome(m[i])
            if len(pal) != 0:
                tripletOutsideBrackets.extend(pal)
        pal = self.hasPalindrome(m[-1])
        if len(pal) != 0:
            tripletOutsideBrackets.extend(pal)
        for el in tripletInBrackets:
            if self.inverse(el) in tripletOutsideBrackets:
                return True
        return False

    def run(self, s):
        count = 0
        for line in s.strip().split('\n'):
            if self.supportsSSL(line):
                count += 1
        return count