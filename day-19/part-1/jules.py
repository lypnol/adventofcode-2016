from submission import Submission

class JulesSubmission(Submission):

    def author(self):
        return 'Jules'

    def run(self, s):
        import math
        nb = int(s.strip())
        return 2*(nb-2**int(math.log(nb, 2)))+1