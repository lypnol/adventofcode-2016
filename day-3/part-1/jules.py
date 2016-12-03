from submission import Submission

class JulesSubmission(Submission):

    def author(self):
        return 'Jules'

    def run(self, s):
        count = 0
        for line in s.rstrip().split('\n'):
            line = line.replace('    ','  ')
            n1,n2,n3 =  sorted(map(int,line.lstrip().rstrip().split('  ')))
            if n1+n2 > n3:
                count += 1
        return count
