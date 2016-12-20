from submission import Submission

class JulesSubmission(Submission):

    def author(self):
        return 'Jules'

    def run(self, s):
        ips = s.strip().split('\n')
        ips = sorted(ips, key=lambda x: int(x.split('-')[0]))
        nb = 0
        for ipRange in ips:
            low,high = map(int,ipRange.split('-'))
            if nb < low:
                return nb
            else:
                nb = max(nb,high + 1)
        return nb
