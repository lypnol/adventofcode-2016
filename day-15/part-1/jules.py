from submission import Submission

class JulesSubmission(Submission):

    def author(self):
        return 'Jules'

    def run(self, s):

        def chinese_remainder(n, a):
            sum = 0
            prod = reduce(lambda a, b: a*b, n)
         
            for n_i, a_i in zip(n, a):
                p = prod / n_i
                sum += a_i * mul_inv(p, n_i) * p
            return sum % prod
         
         
        def mul_inv(a, b):
            b0 = b
            x0, x1 = 0, 1
            if b == 1: return 1
            while a > 1:
                q = a / b
                a, b = b, a%b
                x0, x1 = x1 - q * x0, x0
            if x1 < 0: x1 += b0
            return x1

        n = []
        a = []
        for line in s.strip().split('\n'):
            elements = line.split(' ')
            triplet = ((int(elements[1][1:]),int(elements[3]),int(elements[-1][:-1])))
            n.append(triplet[1])
            a.append(triplet[1]-(triplet[0]+triplet[2]))

        return chinese_remainder(n, a)