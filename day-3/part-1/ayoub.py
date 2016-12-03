from submission import Submission

class AyoubSubmission(Submission):

    def author(self):
        return 'Ayoub'

    def run(self, s):
        def is_triangle(a, b, c):
            return a + b > c and a + c > b and b + c > a

        valid = 0
        for line in s.rstrip().split('\n'):
            a, b, c = list(map(int, line.split()))
            if is_triangle(a, b, c):
                valid += 1

        return valid
