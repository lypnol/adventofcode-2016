from submission import Submission
from md5 import md5

class AyoubSubmission(Submission):

    def author(self):
        return 'Ayoub'

    def run(self, s):
        s = s.rstrip()
        password = list("        ")
        i = 0
        for _ in range(8):
            h = ""
            while True:
                w = s+str(i)
                h = md5(w).hexdigest()
                i += 1
                if str(h[:5]) == "00000" and \
                   ord(h[5]) < ord('8') and ord(h[5]) >= ord('0') and \
                   password[int(h[5])] == ' ':
                        break

            password[int(h[5])] = str(h[6])

        return "".join(password)
