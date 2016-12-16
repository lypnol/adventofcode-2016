from submission import Submission


class AyoubSubmission(Submission):

    def author(self):
        return 'Ayoub'

    def run(self, s):
        s = s.rstrip()

        N = 272

        def dragon_curve(s):
            a = s
            b = list(a[::-1])
            for i in range(len(b)):
                b[i] = str(chr((ord(b[i]) -  ord('0') + 1)%2 + ord('0')))
            return a + '0' + ''.join(b)

        def checksum(s):
            c = ''
            while len(c) % 2 == 0:
                c = ''
                for i in range(0, len(s)-1, 2):
                    if s[i] == s[i+1]:
                        c += '1'
                    else:
                        c += '0'
                if len(c) % 2 == 0:
                    s = c
            return c

        while len(s) < N:
            s = dragon_curve(s)
        s = s[:N]

        return checksum(s)
