from submission import Submission
from md5 import md5

class AyoubSubmission(Submission):

    def author(self):
        return 'Ayoub'

    def run(self, s):
        s = s.rstrip()
        password = ""
        i = 0
        for _ in range(8):
            h = ""
            while True:
                w = s+str(i)
                h = md5(w).hexdigest()
                i += 1
                if str(h[:5]) == "00000":
                        break

            password += str(h[5])

        return "".join(password)
