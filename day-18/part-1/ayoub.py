from submission import Submission


class AyoubSubmission(Submission):

    def author(self):
        return 'Ayoub'

    def run(self, s):
        s = s.rstrip()
        N = 40
        row = s

        def is_safe(x, y, z):
            if x == '^' and y == '.' and z == '.':
                return False
            if z == '^' and y == '.' and x == '.':
                return False
            if z == '^' and y == '^' and x == '.':
                return False
            if x == '^' and y == '^' and z == '.':
                return False
            return True

        i = 1
        count = list(row).count('.')
        while i < N:
            new = ''
            for j in range(len(row)):
                if is_safe(row[j-1] if j > 0 else '.',
                        row[j],
                        row[j+1] if j < len(row)-1 else '.'):
                           new += '.'
                           count += 1
                else:
                    new += '^'
            row = new
            i += 1
        
        return count
