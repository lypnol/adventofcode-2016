from submission import Submission

class AyoubSubmission(Submission):

    def author(self):
        return 'Jules'

    def run(self, s):
        count = 0
        puzzle = s.rstrip().split('\n')
        for i in range(0,len(puzzle),3):
            line1 = map(int,puzzle[i].replace('    ','  ').lstrip().rstrip().split('  '))
            line2 = map(int,puzzle[i+1].replace('    ','  ').lstrip().rstrip().split('  '))
            line3 = map(int,puzzle[i+2].replace('    ','  ').lstrip().rstrip().split('  '))
            for j in range(0,3):
                n1,n2,n3 = sorted([line1[j],line2[j],line3[j]])
                if n1+n2 > n3:
                    count += 1
        return count